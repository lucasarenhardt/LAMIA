from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota+delta
    return calc

notas = [5.5, 7.9, 8.2, 3.1]
notas_finais_1 = list(map(somar_nota(1), notas))
notas_finais_2 = list(map(somar_nota(1.5), notas))

print(notas_finais_1)
print(notas_finais_2)

def somar(a, b):
    return a+b

total = reduce(somar, notas, 0)
print(total)

#for i, nota in enumerate(notas):
#    notas[i] = nota+1.5

#for i, nota in range(len(notas)):
#    notas[i] = notas[i]+1.5

