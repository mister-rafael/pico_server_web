from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"led": "on", "temperatura": 28.5})

@app.route('/comando', methods=['POST'])
def comando():
    data = request.json
    print(f"Comando recebido: {data}")
    return jsonify({"status": "comando recebido"})

@app.route('/mensagem', methods=['GET'])
def enviar_mensagem():
    return jsonify({
        "mensagem": "Olá, Postman! Tudo funcionando direitinho. 🚀"
    })