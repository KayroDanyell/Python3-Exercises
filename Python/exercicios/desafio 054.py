from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0,8):
    nasc = int(input('que ano vc nasceu?:'))
    idade = ano-nasc
    if idade >= 21 :
        maior+=1
    else:
        menor+=1
print(f'O total de pessoas maiores é : {maior}')
print(f'o total de pessoas menores é: {menor}')

