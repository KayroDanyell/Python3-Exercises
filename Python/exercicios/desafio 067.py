n=0
while True:
    n=int(input('quer saber a tabuada de qual valor?'))
    if n<0:
        print('Programa tabuada interrompido')
        break
    for c in range (1,11):
        print(f'{c}x{n}=', n*c)
