-- Cria o banco e a tabela usados por bot/database.py
CREATE DATABASE IF NOT EXISTS chatbot;
USE chatbot;

CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_usuario VARCHAR(50) NOT NULL,   -- número do WhatsApp (ex.: whatsapp:+5562...)
    itens TEXT NOT NULL,                   -- itens separados por vírgula
    total DECIMAL(10, 2) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
