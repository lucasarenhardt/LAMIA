carros = ['Civic', 'Cruze']
adj = ['Sedan', 'Hatch']

for c in carros:
    for a in adj:
        print(f'{c} {a}')

for i in [1,2,3]:
    pass

for i in range(1, 11):
    if(i % 2) == 1:
        continue
    print(i)

for i in range(1, 11):
    if(i == 5):
        break
    print(i)

print('Fim.')