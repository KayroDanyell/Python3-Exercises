q = 's'
trab = dict()
trab['nome'] = input('Qual seu nome?')
nasc = int(input('Que ano voce nasceu?'))
trab['idade'] = 2020-nasc
trab['ctps'] = int(input('numero da cartera de trabalho?'))
if trab['ctps'] != 0:
    trab['ano de contratacao'] = int(input('Em que ano voce foi contratado?'))
    trab['salario'] = int(input('qual seu salario?'))
    apos = ((35-(2020-trab['ano de contratacao']))+trab['idade'])
    trab['aposentadoria'] = apos
print(trab)
