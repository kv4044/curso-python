n = total = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para para]: '))
    if n != 999:
        soma += n
        total += 1
print(f'Você digitou {total} e a soma entre eles foi de {soma}.')
