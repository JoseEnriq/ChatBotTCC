import json
import spacy
from twilio.twiml.messaging_response import MessagingResponse
from bot.utils import loja_aberta, horario_funcionamento, saudacao
from bot.database import salvar_pedido

# Carrega modelo de linguagem do spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Carrega o menu de produtos a partir de um arquivo JSON
with open('data/menu.json', encoding='utf-8') as f:
    MENU = json.load(f)

# Dicionário temporário para armazenar pedidos por número
CARRINHO = {}

# Função para construir o menu em formato de texto
def montar_menu():
    texto = "🍽️ *Cardápio da Loja de Comidas*\n"
    for item in MENU:
        texto += f"{item['id']}. {item['nome']} - R${item['preco']:.2f}\n"
    texto += "\nDigite o número do item para adicionar ao pedido."
    return texto

# Função de PLN para identificar intenção da mensagem
def detectar_intencao(mensagem):
    doc = nlp(mensagem.lower())

    for token in doc:
        if token.lemma_ in ["menu", "cardápio"]:
            return "ver_menu"
        elif token.lemma_ in ["horário", "funcionamento"]:
            return "ver_horario"
        elif token.lemma_ in ["pedido", "carrinho"]:
            return "ver_pedido"
        elif token.lemma_ in ["finalizar", "concluir", "fechar"]:
            return "finalizar_pedido"
        elif token.lemma_ in ["obrigado", "valeu"]:
            return "agradecimento"
        elif token.lemma_ in ["oi", "olá"]:
            return "saudacao"
    return "desconhecido"

# Função principal que processa as mensagens recebidas
def responder_usuario(msg, numero_usuario=None):
    msg = msg.strip().lower()
    resposta = MessagingResponse()

    if numero_usuario not in CARRINHO:
        CARRINHO[numero_usuario] = []

    if msg.isdigit():
        item = next((i for i in MENU if str(i["id"]) == msg), None)
        if item:
            CARRINHO[numero_usuario].append(item)
            resposta.message(f"✅ {item['nome']} adicionado ao pedido.")
        else:
            resposta.message("❌ Item não encontrado.")
        return str(resposta)

    # Usa PLN para detectar a intenção da mensagem
    intencao = detectar_intencao(msg)

    if intencao == "ver_menu":
        resposta.message(montar_menu())

    elif intencao == "ver_horario":
        status = "Estamos *abertos*!" if loja_aberta() else "Estamos *fechados* no momento."
        resposta.message(f"{horario_funcionamento()}\n{status}")

    elif intencao == "saudacao":
        resposta.message(saudacao())

    elif intencao == "ver_pedido":
        if not CARRINHO[numero_usuario]:
            resposta.message("🛒 Seu carrinho está vazio.")
        else:
            resumo = "🧾 *Resumo do seu pedido:*\n"
            total = 0
            for item in CARRINHO[numero_usuario]:
                resumo += f"- {item['nome']} R${item['preco']:.2f}\n"
                total += item['preco']
            resumo += f"\n💰 Total: R${total:.2f}"
            resposta.message(resumo)

    elif intencao == "finalizar_pedido":
        if not CARRINHO[numero_usuario]:
            resposta.message("Seu pedido está vazio. Envie o número do item para adicionar.")
        else:
            total = sum(item['preco'] for item in CARRINHO[numero_usuario])
            itens = ", ".join(item['nome'] for item in CARRINHO[numero_usuario])
            salvar_pedido(numero_usuario, itens, total)
            resposta.message(f"✅ Pedido finalizado!\nItens: {itens}\nTotal: R${total:.2f}")
            CARRINHO[numero_usuario] = []

    elif intencao == "agradecimento":
        resposta.message("😊 De nada! Estamos à disposição.")

    else:
        resposta.message("❓ Não entendi. Envie 'menu', 'horário', número do item ou 'pedido'.")

    return str(resposta)