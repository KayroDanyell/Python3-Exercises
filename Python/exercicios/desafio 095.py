jog = dict()
gols = list()
geral = list()
total = 0
cont = 0
#print('cod nome',' '*5,'gols',' '*5,'total')
while True:
    jog.clear()
    jog['nome'] = str(input('Nome do  jogador:'))
    p = int(input('quantas partidas ele jogou?'))
    for c in range(0,p):
        gols.append(int(input(f'Quantos gols ele fez na {c} partida?')))
    jog['gols'] = gols.copy()
    for s in jog['gols']:
        total += s
    jog['total'] = total
    geral.append(jog.copy())
    q = input('Voce deseja continuar?')
    if q in 'Nn':
        break
print(geral)
print('-'*30)
print('cod nome',' '*5,'gols',' '*15,'total')
for j in geral:
    print(j)
while True:
    pergunta = input('mostrar dados de qual jogador?')
    for l in 