def escrevetxt(txt, idade):
    arq = open('py.txt', 'r')
    cont = arq.readlines()
    cont.append(f'{txt}, ')
    cont.append(idade)
    arq = open('py.txt','w')
    arq.writelines(cont)
    arq = open('py.txt','r')
    return arq.read()

while True:
    print('~'*30)
    print('SISTEMA DE CADASTRO')
    print('~'*30)
    print(' 1-cadastrar alguem\n 2-Ler o documento\n 3-Limpar o Arquivo (IRREVERSIVEL)\n 4-Sair Do Programa')
    com = int(input('O que voce deseja fazer?'))
    if com == 1:
        txt = input('Qual seu nome:')
        idade = input('Qual sua idade:')
        a = escrevetxt(txt, idade)
    elif com == 2:
        arq = open('py.txt','r')
        print(arq.readlines())
    elif com == 3:
        cont = []
        arq = open('py.txt', 'w')
        arq.writelines(cont)
    elif com == 4:
        break
