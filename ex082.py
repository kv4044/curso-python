num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = ' '
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
