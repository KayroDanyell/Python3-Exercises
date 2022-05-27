num = int(input('Digite um numero:'))
tot = 0
for c in range(1,num+1):
    if num %c ==0:
        print('\033[34m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f' O número {num} foi dividido {tot} vezes!')
if tot == 2:
    print("e por isso ele 'primo!")
else:
    print("e por isso ele nao e primo!")
