esco = 0
n = 0
cont = 0
while True:
    esco = input('Impar ou par?').lower()
    n = int(input('qual numero voc escolhe?'))
    if esco == 'impar' and n % 2 == 0:
        print('Voce perdeu!')
        break
    elif esco == 'par' and n % 2 == 0:
        print('Voce ganhou!')
        cont += 1
print(f'você gastou {cont} tentativas!')