# Importa as bibliotecas Flask e SocketIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
import os

# Cria a instância do Flask
app = Flask(__name__)
# Configura o SocketIO para permitir conexões de qualquer origem
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html') # Renderiza o template web/templates/index.html

@app.route('/CLICK_A', methods=['GET', 'POST']) # Define a rota para o comando de clique
# Define uma função para lidar com o evento de clique do botão A
def click_a():
    print("Comando: Botão A, pressionado")
    socketio.emit('command', {'action': 'click_a'})  # Envia comando para ON
    return 'Click command sent', 200 # Retorna resposta HTTP 200

@app.route('/SOLTO_A', methods=['GET', 'POST']) # Define a rota para o comando de solto
def solto_a():
    print("Comando: Botão A, solto")
    socketio.emit('command', {'action': 'solto_a'})  # Envia comando para OFF
    return 'solto command sent', 200

# Ponto de entrada principal da aplicação

# Inicia o servidor Flask com suporte a WebSockets
port = int(os.environ.get("PORT", 10000))
socketio.run(app, host='0.0.0.0', port=port) # Permite conexões de qualquer IP na porta 5000