tupla =  'pao', 1 , 'leite', 2.50, 'cafe', 3, 'chocolate', 5
print(f'{"Tabela De Preços":^30}')
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:-<30}', (tupla[pos+1]))