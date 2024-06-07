def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

somar = soma
#print(somar(4, 1))

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

resultado = operacao_aritmetica(somar, 2, 10)
print(resultado)

resultado = operacao_aritmetica(sub, 15, 7)
print(resultado)

def soma_parcial(a):
    #processamento pesado
    def concluir_soma(b):
        return a+b
    return concluir_soma

resultado_final = soma_parcial(10)(43)
print(resultado_final)

