from datetime import date

ano = int(input('Qual ano quer analizar? Digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year  #pega a data do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} \033[4;32mÉ um ano BISSEXTO.')
else:
    print(f'O ano {ano} \033[4;31mNÃO é um ano BISSEXTO.')
