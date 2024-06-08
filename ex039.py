from datetime import date    #ALISTAMENTO OBRIGATORIO

atual = date.today().year
sexo = str(input('Qual seu sexo [F/M]'))
if sexo == 'M':
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
    if idade < 18:
        falta = 18 - idade
        alis = falta + 2024
        print(f'Ainda falta \033[32m{falta} ano(s)\033[m para seu alistamento.')
        print(f'Seu alistamento será em {alis}.')
    elif idade > 18:
        passou = idade - 18
        alis = atual - passou
        print(f'Você já deveria ter se alistado há \033[4;31m{passou} ano(s).\033[m')
        print(f'Seu alistamento foi em {alis}.')
    elif idade == 18:
        print(f'Você tem que se alistar \033[1;31mIMEDIATAMENTE!')
elif sexo == 'F':
    print('Você não precisa fazer alistamento militar obrigatorio.')