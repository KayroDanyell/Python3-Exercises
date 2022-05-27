produto = 0
preco = 0
soma = 0
caro = 0
barato = 0
cont = 0
stop = 0
while True:
    produto = input('Qual produto voce comprou?')
    preco = int(input('qual preco do produto?'))
    soma += preco
    cont += 1
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = preco
    if preco < barato:
        barato = produto
    stop = str(input('Voce deseja continuar?[S/N]')).upper()
    if stop == 'N':
        break
print(f'O total da compra foi: {soma}')
print(f'Desses produtos {caro} custam mais de 1000 reais e o produto mais barato foi {barato}')
