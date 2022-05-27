import random
num = 1
pc = random.randint(0,10)
tent = int(input('Digite sua tentativa:'))
while tent != pc:
    tent = int(input('Voce errou!\n Tente novamente:'))
    num += 1
print(f'parabens voce acertou o numero é {tent}!')
print(f'Voce usou {num} tentativas!')