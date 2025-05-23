from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Criar arquivo CSV se não existir
if not os.path.exists('presencas.csv'):
    with open('presencas.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Identificação', 'Nome', 'Latitude', 'Longitude', 'Data', 'Hora'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    identificacao = request.form['identificacao']
    nome = request.form['nome']
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    data = datetime.now().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    # Salvar no CSV
    with open('presencas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([identificacao, nome, latitude, longitude, data, hora])

    return '✅ Presença registrada com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
