def leiaint(n):
    while True:
        a = input(n)
        if a.isnumeric():
            print(f'voce acabou de digitar o número"{a}"')
            break
        else:
            print('ERRO! Digite um número inteiro')
    return a

a = leiaint('Digite um número:')
print(a)