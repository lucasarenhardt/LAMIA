for i in range(10):
    print(i, end=' ')

print('')

for i in range(5, 11):
    print(i, end=' ')

print('')

for i in range(1, 230, 5):
    print(i, end=' ')

print('')

for i in range(30, 0, -2):
    print(i, end=' ')

print('')

nums = [0, 5, 10, 15, 20, 25]

for n in nums:
    print(n, end=',')

print('')

texto = 'Civic é muito é massa'

print('')

for letra in texto:
    print(letra, end = ' ')

print('')

for n in {1, 2, 3, 4, 4, 4, 2, 3}:
    print(n, end = ' ')

print('')

carro = {
    'nome': 'Civic',
    'ano': 2004,
    'preco': 25000
}

for atrib in carro:
    print(atrib, carro[atrib])

print('')

for atrib, valor in carro.items():
    print(atrib, valor)

print('')

for valor in carro.values():
    print(valor, end=' ')

print('')

for atrib in carro.keys():
    print(atrib, end=' ')