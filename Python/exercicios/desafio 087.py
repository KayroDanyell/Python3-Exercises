pares = soma = mai = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0,3):
    for l in range(0,3):
        matriz[l][c] = int(input('digitte um valor:'))
        if matriz[l][c] %2 == 0:
            pares += matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
for l in range (0,3):
    soma +=  matriz[l][2]
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c]>mai:
        mai = matriz[1][c]
print(f'a soma dos valores pares sao {pares}')
print(f' o maior valor da segunda coluna é {mai}')
print(f'a soma de todos os valores da tercera coluna é {soma}')
