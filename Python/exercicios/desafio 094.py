pessoas = list()
pessoa = dict()
cont = media = 0
mulheres = list()
maioridade = list()
while True:
    pessoa.clear()
    pessoa['nome'] =str(input( 'qual seu nome?'))
    cont += 1
    sexo = str(input('qual seu sexo?')).upper()
    if sexo in 'MmFf':
        pessoa['sexo'] = sexo
    else:
        print('Erro! Digite M ou F!')
        sexo = str(input('Qual seu sexo? Somente M ou F'))
    idade = int(input('Qual sua idade?'))
    media += idade/cont
    pessoa['idade'] = idade
    pessoas.append(pessoa.copy())
    q = str(input('Voce deseja continuar?'))
    if q in 'Nn':
        break
print(pessoas)
print(f'foram registradas {cont} pessoas')
print(f'a media de idade é {media}')
print(f'as pessoas acima da media de idade sao') #NAO TA FUNCIONANDO
for i in pessoas:
    if i['idade'] > media:
        print(i['nome'])
print(f'as mulheres sao ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(p['nome'])
