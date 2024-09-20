import csv
from datetime import datetime

# Nome do arquivo CSV para armazenar os dados
FILENAME = 'recursos.csv'

# Função para inicializar o arquivo CSV se não existir
def inicializar_arquivo():
    try:
        with open(FILENAME, mode='r') as file:
            pass  # Arquivo já existe
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Quantidade', 'Data', 'Responsável', 'Tipo'])  # Cabeçalhos do CSV

# Função para registrar entrada ou saída de recursos
def registrar_recurso(nome, quantidade, responsavel, tipo):
    data = datetime.now().strftime('%d/%m/%Y')
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, quantidade, data, responsavel, tipo])
    print(f"Recurso '{nome}' {tipo} registrado com sucesso!")

# Função para gerar um relatório dos recursos
def gerar_relatorio():
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

    print("\nRelatório de Recursos:")
    for nome, quantidade in recursos.items():
        print(f"Recurso: {nome}, Quantidade Disponível: {quantidade}")

# Inicializa o arquivo CSV
inicializar_arquivo()

# Interface simples no terminal
while True:
    print("\n1. Registrar Entrada de Recurso")
    print("2. Registrar Saída de Recurso")
    print("3. Gerar Relatório")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Nome do recurso: ")
        quantidade = input("Quantidade: ")
        responsavel = input("Responsável pela entrada: ")
        registrar_recurso(nome, quantidade, responsavel, 'Entrada')
    elif escolha == '2':
        nome = input("Nome do recurso: ")
        quantidade = input("Quantidade: ")
        responsavel = input("Responsável pela saída: ")
        registrar_recurso(nome, quantidade, responsavel, 'Saída')
    elif escolha == '3':
        gerar_relatorio()
    elif escolha == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
