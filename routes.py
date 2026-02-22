# Importa módulos necessários do Flask e função para responder o usuário
from flask import Blueprint, request, Response
from bot.responder import responder_usuario

# Cria um blueprint para organizar as rotas
routes = Blueprint('routes', __name__)

# Define a rota que receberá as mensagens do WhatsApp via POST
@routes.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get('Body')  # Pega o texto da mensagem
    numero = request.form.get('From')  # Pega o número do usuário
    print(f"Mensagem recebida de {numero}: {msg}")  # Exibe no console para debug
    resposta = responder_usuario(msg, numero)  # Gera a resposta com base na mensagem recebida
    return Response(resposta, mimetype="application/xml")  # Retorna a resposta no formato XML