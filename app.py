from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

ADMIN_PASSWORD = "051012"
CSV_FILE = "presencas.csv"

# Garante que o CSV exista
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nome', 'CPF/RA', 'Curso', 'Turma', 'Externo Info', 'Latitude', 'Longitude'])

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None
    if request.method == 'POST':
        nome = request.form['nome']
        cpf_rh = request.form['cpf_rh']
        curso = request.form['curso']
        turma = request.form['turma']
        externo_info = request.form['externo_info']
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([nome, cpf_rh, curso, turma, externo_info, latitude, longitude])

        success_message = "✅ Presença registrada com sucesso!"

    return render_template('index.html', success_message=success_message)

@app.route('/admin', methods=['GET'])
def admin():
    senha = request.args.get('senha')
    if senha != ADMIN_PASSWORD:
        return "❌ Acesso negado. Senha incorreta.", 403

    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        presencas = list(reader)

    return render_template('admin.html', presencas=presencas)

if __name__ == "__main__":
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
