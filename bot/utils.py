# Importa a biblioteca para trabalhar com data e hora
from datetime import datetime

# Importa configurações de horário e dias de funcionamento
from config import HORARIO_ABERTURA, HORARIO_FECHAMENTO, DIAS_ABERTOS

# Função que verifica se a loja está aberta no momento
def loja_aberta():
    agora = datetime.now()
    hora = agora.hour
    dia_semana = agora.weekday()
    return (HORARIO_ABERTURA <= hora < HORARIO_FECHAMENTO) and (dia_semana in DIAS_ABERTOS)

# Função que retorna o texto de horário de funcionamento da loja
def horario_funcionamento():
    return "🕐 Estamos abertos de Segunda a Sábado, das 10h às 22h."

# Função que retorna uma mensagem de saudação
def saudacao():
    return "Olá! 👋 Bem-vindo à nossa loja de comidas. Envie 'menu' para ver o cardápio!"