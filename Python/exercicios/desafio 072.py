tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
while True:
    num = int(input('Qual numero ,entre 0 e 20, voce deseja ver em extenso?'))
    if num>=0 and num<=20:
        print(tupla[num])
    else:
        print('tente novamente. DIgite um numero entre 0 e 20')