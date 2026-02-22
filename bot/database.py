# Importa o conector do MySQL para permitir interação com o banco de dados
import mysql.connector

# Função para estabelecer a conexão com o banco de dados MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Usuário do banco de dados
        password="password",  # Senha do banco de dados
        database="chatbot"    # Nome do banco de dados
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