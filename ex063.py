print('-'*25)
print('\033[35mSEQUÊNCIA DE FIBONACCI\033[m')
print('-'*25)
termo = int(input('Quantos termos você quer da sequência? '))
print('~*'*15)
a = 0
b = 1
cont = 3
print(f'{a} → {b}', end=' → ')
while cont <= termo:
    c = a + b
    print(c, end=' → ')
    a = b
    b = c
    cont += 1
print('FIM')
print('~*'*15)
