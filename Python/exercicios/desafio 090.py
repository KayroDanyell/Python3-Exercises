alunos = list()
nome = dict()
m = 0
while True:
    nome['nome'] = (input('Qual o nome do aluno?'))
    nome['media'] = int((input('qual a media do aluno?')))
    m = nome['media']
    print(nome['media'])
    if m >= 7:
        nome['situacao'] = 'aprovado'
    else:
        nome['situacao'] = 'reprovado'
    alunos.append(nome.copy())
    q = input('voce deseja continuar?')
    if q in 'Nn':
        break
print(f'{alunos}')
vis = int(input(f'de {len(alunos)} alunos, qual aluno voce deseja visualizar ?'))
print(alunos[vis])
