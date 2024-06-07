from functools import reduce

carros = [
    {'nome': 'Civic', 'ano': 2004},
    {'nome': 'Cruze', 'ano': 2020},
    {'nome': 'Ranger', 'ano': 2018},
    {'nome': 'Uno', 'ano': 2000},
    {'nome': 'Sandero', 'ano': 2016},
]

carro_atual = lambda carro: carro['ano'] > 2015
obter_ano = lambda carro: carro['ano']
somar = lambda a, b: a+b

carros_atuais = [carro for carro in carros if carro['ano'] > 2015]
ano_carros_atuais = [carro['ano'] for carro in carros_atuais]

print(ano_carros_atuais )
