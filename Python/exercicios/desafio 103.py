def ficha(j =0, g=0):
    if j == '':
        print(f'o jogador (desconhecido) marcou {g} gols')
    else:
        print(f'o jogador {j} marcou {g} gols')


j = str(input('o nome do jogador:'))
g = int(input('quantos gols:'))
ficha(j, g)
