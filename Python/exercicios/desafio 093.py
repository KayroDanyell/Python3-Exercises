jog = dict()
gols = list()
total = 0
cont = 0
jog['nome'] = str(input('Nome do  jogador:'))
p = int(input('quantas partidas zico jogou?'))
for c in range(0,p):
    gols.append(int(input(f'Quantos gols ele fez na {c} partida?')))
jog['gols'] = gols
for s in gols:
    total += s
jog['total'] = total
print(jog)
print('_-'*30)
print(f'O campo nome tem o valor {jog["nome"]}')
print(f'o campo gols tem o valor {jog["gols"]}')
print(f'o campo total tem o valor {jog["total"]}')
print('~'*30)
print(f'O jogador {jog["nome"]} jogou {p} partidas')
for g in jog['gols']:
    print(f'na partida{cont+1},fez {g} gols')
print(f' foi um total de {jog["total"]} gols' )