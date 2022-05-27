from time import sleep
n1 = int(input('insira aqui um número:'))
n2 = int(input('insira aqui outro número:'))
fun = 0
while not fun == 5:
    print('''=====MENU=====\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa''')
    fun = int(input('insira aqui su alternativa: '))
    if fun == 1:
        print("Voce escolheu soma!\n E o resultado é:", n1+n2)
        print('Reiniciando...')
        sleep(1)
    elif fun == 2:
        print('Voce escolheu Multiplicação!\n Eo seu resultado é:', n1*n2)
        print('Reiniciando...')
        sleep(1)
    elif fun == 3:
        if n1>n2:
            print(f"{n1} é maior que {n2}")
            print('Reiniciando...')
            sleep(1)
        elif n2>n1:
            print(f'{n2}é maior que {n1}')
            print('Reiniciando...')
            sleep(1)
        else:
            print(f'{n1} é igual a {n2}')
            print('Reiniciando...')
            sleep(1)
    elif fun == 4:
        n1 = int(input('insira aqui um novo número:'))
        n2 = int(input('insira aqui um novo número:'))
        print('Reiniciando...')
        sleep(1)
