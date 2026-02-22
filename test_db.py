from bot.database import conectar_mysql

try:
    conn = conectar_mysql()
    if conn.is_connected():
        print("✅ Conexão com o MySQL foi bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar no MySQL:")
    print(e)