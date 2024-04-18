import csv

def init_csv(filename='dados_filtrados.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Defina seus cabeçalhos aqui
        headers = ['Tempo', 'ID', 'Valor Filtrado']
        writer.writerow(headers)

def save_to_csv(dados_filtrados, filename='dados_filtrados.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dados_filtrados)
