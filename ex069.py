totidade = toth = totm20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    print('-'*20)
    if idade >= 18:
        totidade += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totidade}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm20} mulher com menos de 20 anos.')
