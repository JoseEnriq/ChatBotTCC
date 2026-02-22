# Importa a classe Flask e o blueprint de rotas
from flask import Flask
from routes import routes

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Registra as rotas definidas no blueprint
app.register_blueprint(routes)

# Inicia o servidor quando o script for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)