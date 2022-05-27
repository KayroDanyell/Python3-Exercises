lixta = []
for c in range(0,7):
    lixta.append(int(input('Digite um número:')))
print(lixta)
print(f'o maior numero da lista é: {max(lixta)} e sua posicao é {lixta.index(max(lixta))}')
print(f'o menor numero da lista é: {min(lixta)} e sua posicao é {lixta.index(min(lixta))}')