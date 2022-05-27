from Utilidadescev import moeda
v = int(input('insira um valor:'))
print(f'a metade de {v}, é {moeda.moeda(moeda.metade(v), moeda ="$", p = True)}')
moeda.resumo(v, 50, 30)
