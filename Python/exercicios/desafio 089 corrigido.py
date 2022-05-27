ficha = list()
while True:
    nome = str(input('nome do aluno:'))
    nota1 = int(input('nota 1 :'))
    nota2 = int(input('nota 2 :'))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(ficha)
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<Volte Sempre!')


