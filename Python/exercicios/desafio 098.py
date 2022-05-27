import pytube
def contador(a,b,c):
    for s in range(a,b,c):
        print(s)


a= int(input('insira aqui o inicio da contagem:'))
b= int(input('fim da contagem:'))
c = int(input('passo da contagem:'))
contador(a,b,c)

video = pytube.YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
