boletim = list()
aluno = list()
notas = list()
q = 's'
#LISTA ESTÁ COMPLETA E FUNCIONANDO
while q == 's':
    aluno.append(input('Digite aqui o nome do aluno:'))
    for c in range(0,2):
        notas.append(int(input('digite aqui a nota do aluno:')))
    aluno.append(notas[:])
    boletim.append(aluno[:])
    notas.clear()
    aluno.clear()
    q = str(input('Voce deseja continuar?[s/n]')).lower()
    if q == 'n':
        break
print('Num',''*5)
print(aluno)
print(notas)
print(boletim)
