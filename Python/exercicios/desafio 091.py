import random
from operator import itemgetter
cont=0
jogos = {}
for j in range (1,5):
    jogos[f'jogador {j}'] = random.randrange(1,7)
print('VALORES SORTEADOS:')
for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado')
rank = {}
print(f'a ordem de ganhadores é: ')
rank = sorted(jogos.items(),key=itemgetter(1), reverse=True)
print(rank)
for c,n in enumerate(rank):
   print(f'{c+1} lugar com o valor {n[1]}')
#print(f' {jogos.keys(n)} com ó número {n} em {cont} lugar')

