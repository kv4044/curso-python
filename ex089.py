alunos = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    resp = ' '
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N) ')).strip().upper()
    if resp == 'N':
        break
print('=-'*40)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    qual = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if qual == 999:
        break
    if qual <= len(alunos) - 1:
        print(f'Notas de {alunos[qual][0]} são {alunos[qual][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
