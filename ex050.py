s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}o numero: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Voce informou {cont} numeros PARES e a soma foi {s}.')
