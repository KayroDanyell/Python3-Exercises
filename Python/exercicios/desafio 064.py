soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('insira um número:'))
    soma += n
    cont += 1
soma -= 999
cont -= 1
print(f'foram digitados {cont} números e a soma entre eles foi de {soma}')
