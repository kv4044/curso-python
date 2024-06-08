valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if maior < valores[c]:
            maior = valores[c]
        if menor > valores[c]:
            menor = valores[c]
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
