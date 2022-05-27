def leiadinheiro(a = ('Digite um numero:')):
    while True:
        msg = input(a)
        if msg.isnumeric():
            break
        else:
            print('ERRO! Digite apenas números!')
    return msg

a = ('Digite um numero:')
p = leiadinheiro(a)