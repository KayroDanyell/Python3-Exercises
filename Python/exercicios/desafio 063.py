n1 = int(input('insira aqui um número:'))
n2 = int(input('insira aqui putrp numero:'))
cont = int(input('quantos termos voce deseja na sua sequencia?' ))
while cont>0:
    soma= n1+n2
    n1=n2
    n2=soma
    cont-=1
    print (n2)