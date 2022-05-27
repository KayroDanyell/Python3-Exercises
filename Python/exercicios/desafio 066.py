n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um númerp:'))
    if n == 999:
        break
    cont+=1
    soma += n
print(f'forma digiados {cont} numeros e a soma entre eles foi de {soma} ')
