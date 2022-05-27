exp = str(input('Digite sua expressão:'))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)>0:
    print('sua expressao esta errada!')
else:
    print('sua expressao esta correta!')