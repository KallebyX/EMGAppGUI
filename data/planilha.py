import csv

def init_csv(filename='dados_filtrados.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ['Tempo', 'ID', 'Valor Filtrado']
        writer.writerow(headers)

def save_to_csv(dados_filtrados, filename='dados_filtrados.csv'):
    if not isinstance(dados_filtrados, list) or not all(isinstance(item, (int, float, str)) for item in dados_filtrados):
        raise ValueError("Dados filtrados devem ser uma lista de inteiros, floats ou strings.")
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(dados_filtrados)
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")

