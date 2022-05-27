lixta = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor:'))
    lixta.append(valor)
    if valor %2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    quest = str(input('Voce deseja continuar?')).lower()
    if quest == 'n':
        break
print(f'os numeros digitados foram {lixta}')
print(f'on numeros pares digitado foram {par}')
print(f'os numeros impares digitados foram{impar}')