import datetime
def voto(a):
    ano = datetime.date.today()
    idade = ano.year - a
    if idade>=18 and idade<100:
        return('Voto Obrigatorio!')
    elif idade>=16 and idade<18:
        return('Voto opcional!')
    else:
        return('Voto negado!')


nasc = int(input("que ano voce nasceu?"))
idade =voto(nasc)
print(idade)
