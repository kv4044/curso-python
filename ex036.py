print('-=-'*10)
print('\033[1;33mFINANCIAMENTO DE UMA CASA\033[m')
print('-=-'*10)
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)  #parcela por mes
minimo = sal * 30 / 100  #30% do salario
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${parcela:.2f} por mês.')
if parcela <= minimo:
    print('Empréstimo: \033[32mAPROVADO\033[m!')  #Emprestimo aprovado
else:
    print('Empréstimo: \033[31mNEGADO\033[m!')  #Emprestimo negado
