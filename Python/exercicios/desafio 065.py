n = 0
media = 0
soma = 0
maior= 0
menor = 0
cont = 0
stop = 'SIM'
while stop == 'SIM':
    n = int(input('digite um numero:'))
    soma += n
    cont += 1
    media = soma/cont
    if cont == 1:
        menor = n
        maior = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    if cont %10 == 0:
        stop = str(input('voce deseja continuar?: [sim/nao]')).upper()
print(f'a média foi de {media}, maior número foi {maior} e o menor número foi {menor}')



