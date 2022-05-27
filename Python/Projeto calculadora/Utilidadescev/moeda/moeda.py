def aumentar(a, p):
    pct = p/100
    a += a*pct
    return (a)

def diminuir(a, p):
    pct = p / 100
    a -= a * pct
    return (a)

def dobro(a):
    a = a * 2
    return a

def metade(a):
    a = a / 2
    return a

def moeda(preco=0, moeda='R$', p=False):
    # preco = float(input('digite um valor:'))
    if not p:
        return f'{preco:.2f}'.replace('.', ',')
    else:
        return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(p, b, c):
    print('-' * 20)
    print('RESUMO DO VALOR')
    print('-' * 20)
    print(f'Preco analisado: {p}')
    print(f'Dobro do Preço: {dobro(p)}')
    print(f'Metade do preco: {metade(p)}')
    print(f'{b}% de aumento: {aumentar(p, b)}')
    print(f'{c}% de diminuir: {diminuir(p, c)}')
