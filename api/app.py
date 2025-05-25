from flask import Flask, render_template, request

# Cria a instância do Flask
app = Flask(__name__)

@app.route('/')
def home(): # Rota para a página inicial index.html
    return render_template('index.html')
