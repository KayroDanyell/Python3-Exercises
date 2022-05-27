
def maior(*num):
    maiorv = 0
    print(f'para {num}')
    for c in num:
        if c>maiorv:
            maiorv=c
    print(f'o maior numero é {maiorv}')
    print('='*30)


maior(1,2,3,4,5)
maior(3,4,6,89,234,55)