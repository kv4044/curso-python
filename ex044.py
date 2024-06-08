print(f'{'JEFFIMAK':=^30}')    #SISTEMA DEDESCONTO E JUROS
preco = float(input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção '))
if opcao == 1:
    novo = preco-(preco*10/100)
elif opcao == 2:
    novo = preco-(preco*5/100)
elif opcao == 3:
    novo = preco
    parcela = novo / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    novo = preco+(preco*20/100)
    valor = novo / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor:.2f} COM JUROS.')
else:
    novo = 0
    print('\033[1;31mERRO OPÇÃO INEXISTENTE!!\033[m')
print(f'Sua compra de R${preco:.2f} vai custar R${novo:.2f} no final.')
