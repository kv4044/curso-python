num = list()
# cont = 0
while True:
    # cont += 1
    n = int(input('Digte um valor: '))
    if n not in num:
        print('Valor adicionado com sucesso...')
        num.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('=-'*30)
num.sort()
print(f'Voce digitou os valores {num}')
