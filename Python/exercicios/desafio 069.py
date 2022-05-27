homens = 0
mulher20 = 0
idade = 0
sexo = 0
menor = 0
stop = 'SIM'
while True:
    idade = int(input('qual sua idade?'))
    sexo = str(input('qual seu sexo? [F/M]')).upper()
    if sexo == 'M':
        homens += 1
    if sexo =='F' and idade<20:
        mulher20 += 1
    if idade < 18:
        menor += 1
    stop = str(input('Voce deseja  continuar ?')).upper()
    if stop == 'NAO':
            break
print(f'Ao todo foram {menor} pessoas menor de 18 anos')
print(f"Foram registrados {homens} homens")
print(f'Foram registrados {mulher20} mulheres menores de 20 anos')


