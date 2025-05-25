# Importa as bibliotecas Flask e SocketIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

# Cria a instância do Flask
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Servidor Flask-SocketIO está no ar!"

@socketio.on('mensagem')
def handle_message(data):
    print(f"Mensagem recebida: {data}")
    emit('resposta', {'resposta': 'Recebido com sucesso!'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)