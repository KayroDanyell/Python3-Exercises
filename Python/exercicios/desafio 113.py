def leiaint(n = 0):
    while True:
        try:
            a = int(input('Digite um numero:'))
            print(f'voce acabou de digitar o número"{a}"')
            break
        except (ValueError, TypeError) :
            print('ERRO! Houve um erro com os valores que voce digitou!')

        except Exception as erro:
            print(f'foi encontrado um problema: {erro.__class__}')
    return a
leiaint('Digite um numero')
