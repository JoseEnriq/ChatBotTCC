# Importa o conector do MySQL para permitir interação com o banco de dados
import os

import mysql.connector
from dotenv import load_dotenv

# Lê as credenciais do banco do arquivo .env (veja .env.example)
load_dotenv()

# Função para estabelecer a conexão com o banco de dados MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),           # Usuário do banco de dados
        password=os.getenv("MYSQL_PASSWORD", ""),       # Senha do banco de dados
        database=os.getenv("MYSQL_DATABASE", "chatbot")  # Nome do banco de dados
    )

# Função para salvar um pedido no banco de dados
def salvar_pedido(numero_usuario, itens, total):
    conn = conectar_mysql()  # Conecta ao banco
    cursor = conn.cursor()   # Cria um cursor para executar comandos SQL
    sql = "INSERT INTO pedidos (numero_usuario, itens, total) VALUES (%s, %s, %s)"
    cursor.execute(sql, (numero_usuario, itens, total))  # Executa o comando de inserção
    conn.commit()    # Confirma a transação
    cursor.close()   # Fecha o cursor
    conn.close()     # Fecha a conexão
