from flask import Flask, request, render_template, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)
FILENAME = 'recursos.csv'

def inicializar_arquivo():
    try:
        with open(FILENAME, mode='r') as file:
            pass
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Quantidade', 'Data', 'Responsável', 'Tipo'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        responsavel = request.form['responsavel']
        tipo = request.form['tipo']
        data = datetime.now().strftime('%d/%m/%Y')

        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, quantidade, data, responsavel, tipo])

        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/relatorio')
def relatorio():
    recursos = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nome = row['Nome']
            quantidade = int(row['Quantidade'])
            tipo = row['Tipo']
            if nome not in recursos:
                recursos[nome] = 0
            if tipo == 'Entrada':
                recursos[nome] += quantidade
            elif tipo == 'Saída':
                recursos[nome] -= quantidade

    return render_template('relatorio.html', recursos=recursos)

if __name__ == '__main__':
    inicializar_arquivo()
    app.run(debug=True)
