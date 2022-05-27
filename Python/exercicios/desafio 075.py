tupla = int(input('digite um numero:')),int(input('digite um numero:')),int(input('digite um numero:')),\
        int(input('digite um numero:')),
print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o valor 3 apareceu pela primeira vez na posicao {tupla.count(3)}')
print(f'Os numeros pares foram' , end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
