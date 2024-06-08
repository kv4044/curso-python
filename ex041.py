from datetime import date  #BGLH DE ATLETA
atual = date.today().year
ano = int(input('Ano nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 25:
    print('Classificação: MASTER')
