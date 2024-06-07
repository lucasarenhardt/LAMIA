ano = int(input('Informe o ano do carro: '))

if(ano <= 2004):
    print('Seu carro ja possui 20 anos ou mais')
elif(2004 < ano < 2014):
    print('Seu carro possui entre 10 a 20 anos')
else:
    print('Seu carro possui 10 anos ou menos')

print(ano)