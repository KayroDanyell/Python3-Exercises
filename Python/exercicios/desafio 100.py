import random
def sorteio (a):
    for s in range(0,5):
        a.append(random.randint(0,10))
    print(a)
def somapar (lista):
    soma = 0
    for c in lista:
        if c %2 == 0:
            soma += c
    print(f'a soma dos pares é {soma}')


lista = list()
sorteio(lista)

somapar(lista)