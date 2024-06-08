sal = float(input('qual é o salário do funcionário? R$'))
if sal <= 1250:
    novosal = (sal*15/100)+sal
else:
    novosal = (sal*10/100)+sal
print(f'O novo salário do funcionário vai ser \033[32mR${novosal:.2f}')
