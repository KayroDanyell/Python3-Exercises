print('Descobrindo as notas da primeira etapa:')
notas = dict()
while True:
    Materia = str(input('Qual materia?'))
    x = float(input('Digite aqui a nota da segunda etapa:'))
    nota = float(x*25)/35
    notas[Materia] = nota
    quest = input('Voce deseja continuar?')
    soma = x+nota
    if quest in 'Nn':
        break
for c,v in notas.items():
    print(f'na matéria de {c} a nota foi {v:2} e a soma foi de {soma}')
