n = int(input('digite um numero para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')

while c > 0:              #com while
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

'''for c in range(n, 1, -1):    #com for
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c'''
print(f'= {f}')
