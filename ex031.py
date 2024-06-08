km = float(input('Qual a distância da sua viagem? '))
'''if 200 > km:
    preco = km * 0.50
else:
    preco = km * 0.45'''  # if e else maior
preco = km * 0.50 if km <= 200 else km * 0.45  # if e else menor
print(f'Pela viagemde \033[34m{km}Km\033[m o preço total a pagar é de \033[32mR${preco:.2f}')
