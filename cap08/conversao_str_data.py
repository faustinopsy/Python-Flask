from datetime import datetime

data_string = input('Entre com uma data, no formato mm/dd/yyyy: ')
print('Voce forneceu: ', data_string)

uma_data = datetime.strptime(data_string, '%d/%m/%Y')
print('Apos a conversao, a data fornecida contem:')
print(f'Dia: {uma_data.day}')
print(f'Mes: {uma_data.month}')
print(f'Ano: {uma_data.year}')
