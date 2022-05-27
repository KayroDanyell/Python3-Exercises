velho = 0
mulheres = 0
média = 0
for c in range(1, 5):
    nome = str(input('insira aqui seu nome:'))
    idade = int(input('Insira aqui sua idade:'))
    sexo = str(input('ínsira aqui seu sexo[M/F]:'))
    média += idade
    if c == 1 and sexo == 'M':
        velho=idade
    if sexo == 'M' and idade>velho:
        velho = idade
        maisvelho = c
    if sexo == 'F' and idade < 20:
        mulheres +=1

medidade = média/4
print(f"a média de idade do grupo foi: {medidade}")
print(f'O homem mais velho foi:{maisvelho}')
print(f'o numero de mulheres abaixo de 20 anos é:{mulheres}')