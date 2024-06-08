matiz = [[], [], []]
n = par = scol = tot2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matiz[l].append(n)
        if n % 2 == 0:  # soma dos pares
            par += n
print('=-' * 30)
for c in range(0, 3):
    print(f'{matiz[c]}')
print('=-'*30)
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    scol += matiz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matiz[1][c]
    elif matiz[1][c]>maior:
        maior = matiz[1][c]
print(f'O maior valor da segunda linha é {maior}')
