frase = input('insira aqui a sua frase para verifica-la:')
palavras = frase.split()
junto = '' .join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso==junto:
    print('Este é um palindromo!')
else:
    print('este nao e um palindromo!')
