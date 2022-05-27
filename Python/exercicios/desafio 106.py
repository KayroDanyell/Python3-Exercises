def inhelp(a):
    while True:
        a = input('digite o comando q deseja receber ajuda:')
        print('~'*30)
        print('\033[0;30;41m Sistema interativo de ajuda\n')
        print('~' * 30)
        print('='*30)
        help(a)
        print('='*30)
        q = input('deseja continuar?')
        if q in 'Nn':
            print('FIM')
            break

a = 0
inhelp(a)