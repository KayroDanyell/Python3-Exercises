lixta = list()
par = list()
impar = list()
for c in range(0,8):
    valor = int(input('Digite um valor:'))
    if valor %2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
lixta.append(impar[:])
lixta.append(par[:])
print(sorted(lixta))
print(f'os numeros pares sao: {sorted(par)}')
print(f' os numeros impares sao: {sorted(impar)}')



