import random
lixta = list()
palpite = list()
n = int(input('quantos palpites voce quer dar?'))
for l in range(0,n):
    for c in range(0,6):
        add = palpite.append(random.randint(0,61))
        if add in palpite:
            palpite.pop(add)
    lixta.append(palpite[:])
    palpite.clear()
for i, l in enumerate(lixta):
    print(f'os palpite {i+1} foi: {l}')
