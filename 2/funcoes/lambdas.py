from functools import reduce

carros = [
    {'nome': 'Civic', 'ano': 2004},
    {'nome': 'Cruze', 'ano': 2020},
    {'nome': 'Ranger', 'ano': 2018},
    {'nome': 'Uno', 'ano': 2000},
    {'nome': 'Sandero', 'ano': 2016},
]

carro_atual = lambda carro: carro['ano'] > 2015
#carro_quaseNovo = lambda carro: carro['ano'] >= 2020
obter_ano = lambda carro: carro['ano']
somar = lambda a, b: a+b

carros_atuais = list(filter(carro_atual, carros))
#carros_quaseNovos = list(filter(carro_quaseNovo, carros))
ano_carros_atuais = list(map(obter_ano, carros_atuais)) 
total = reduce(somar, ano_carros_atuais, 0)

print(ano_carros_atuais)
print(total / len(carros_atuais))

