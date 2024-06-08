tudo = list()
temp = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(tudo) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    tudo.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(tudo)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in tudo:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in tudo:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
