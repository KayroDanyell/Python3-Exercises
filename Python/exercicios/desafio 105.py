def notas(*num):
    notas = list(num)
    situacao = dict()
    total = maior = media = menor = 0
    for c in notas:
        total += 1
        #print(c)
        media += c
        situacao['media'] = media
        if c == 0:
            maior=c
            menor=c
        if c>maior:
            maior = c
        elif menor<c :
            menor = c
    situacao['media'] = media/total
    situacao['total'] = total
    situacao['menor'] = menor
    situacao['maior'] = maior
    s = input('Voce deseja saber a situacao do aluno?')
    if s in 'Ss':
        if media>6:
            print('aluno aprovado!')
        else:
            print('Aluno reprovado!')
    return situacao
d = notas(5,5,10,30)
print(d)
