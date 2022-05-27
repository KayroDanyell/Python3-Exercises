pt = int(input('insira aqui o primeiro termo da sua PA:'))
raz = int(input('insira aqui a razao da sua PA:'))
pa = 0
fim = 0
while  fim < 10:
    pt+= raz
    fim += 1
    print(pt)
    if fim == 10:
        termo = int(input('voce deseja analisar mais termos?'))
        if termo !=0:
            pt = int(input('insira aqui o primeiro termo da sua PA:'))
            raz = int(input('insira aqui a razao da sua PA:'))
            fim = 0