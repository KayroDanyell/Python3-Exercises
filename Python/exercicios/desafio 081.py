lixta = []
while True:
    valor = int(input('Digite um valor'))
    lixta.append(valor)
    quest = str(input('voce deseja continuar?')).lower()
    if quest == 'n':
        break
print(f'foram digitados {len(lixta)} objetos')
lixta.sort(reverse=True)
print(f'os valores em decrescente sao {lixta}')
if 5 in lixta:
    print('O valor "5" foi digitado e esta na lista')

