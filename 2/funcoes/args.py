def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs):
    status = 'aprovado para compra' if kwargs['km'] < 150000 else 'reprovado para compra'
    return f'{kwargs["nome"]} foi {status}'