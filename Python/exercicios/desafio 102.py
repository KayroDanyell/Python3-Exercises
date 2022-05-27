def fatorial(n, show= False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
            f *= c
        else:
            f *= c
    return(f)



fat = fatorial(5, show=True)
print(fat)