from datetime import datetime
tudo = {'Nome': str(input('Nome: '))}
ano = int(input('Ano de nascimento: '))
tudo['Idade'] = datetime.now().year - ano
tudo['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if tudo['Ctps'] != 0:
    tudo['Contratação'] = int(input('Ano de contratação: '))
    tudo['Salário'] = float(input('Salário: R$'))
    tudo['Aposentadoria'] = tudo['Idade'] + (tudo['Contratação'] + 35) - datetime.now().year
print('=-'*30)
for k, v in tudo.items():
    print(f'   -{k} tem o valor {v}')
