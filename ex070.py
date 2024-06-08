total = maior = menor = totcompra = 0
barato = ''
print('-'*40)
print('LOJA SUPER BARATÃO'.center(35))
print('-'*40)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    totcompra += 1
    if preco > 1000:
        maior += 1
    if totcompra == 1 or preco < menor:
        barato = nome
        menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior} produtos custando mais que R$1000.00')
print(f'O pruduto mais barato foi {barato} que custa R${menor:.2f}')
