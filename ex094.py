medidade = idade = 0

tudo = list()
dado = dict()
while True:
    dado['Nome'] = str(input('Nome: '))
    while True:
        dado['Sexo'] = str(input('Sexo: [M/F]')).upper().strip()
        if dado['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dado['idade'] = int(input('Idade:'))
    idade += dado['idade']
    tudo.append(dado.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N!')
    if resp == 'N':
        break
print(tudo)
print('=-'*30)
print(f'A) Ao todo temos {len(tudo)} pessoas cadastradas.')
medidade = idade / len(tudo)
print(f'B) A média de idade é de {medidade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in tudo:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in tudo:
    if p['idade'] >= medidade:
        print('     ', end='')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
        print()
print('<< ECERRADO >>')
