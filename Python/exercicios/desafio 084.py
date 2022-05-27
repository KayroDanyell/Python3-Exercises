pessoa = list()
dado = list()
cont = 0
totpes = list()
totlev = list()
Q = 's'
while Q == 's':
    dado.append(input('Qual seu nome?'))
    dado.append(int(input('Qual seu peso?')))
    pessoa.append(dado[:])
    cont+=1
    dado.clear()
    Q = str(input('Voce deseja continuar?'))
for p in pessoa:
    if p[1] >= 80:
        totpes.append(p[0])
    else:
        totlev.append(p[0])
print(f'Foram cadastradas {cont} pessoas')
print(f'as pessoas mais pesadas sao {totpes}')
print(f'as pessoas mais leves sao {totlev}')


