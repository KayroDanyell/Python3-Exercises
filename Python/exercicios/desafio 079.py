lixta = []
while True:
    valor = int(input('Digite um valor:'))
    if valor in lixta:
        valor = int(input('Esse valor já foi digitado! Digite outro:'))
    lixta.append(valor)
    quest = str(input('Voce deseja continuar?[S/N')).lower()
    if quest == 'n':
        break
print(sorted(lixta))
