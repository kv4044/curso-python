print('-=-'*9)
print('\033[34mAnalizador de Triângulos\033[m ')
print('-=-'*9)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos a cima \033[32mPODEM FORMAR\033[m triângulos!')
else:
    print('Os segmentos a cima \033[31mNÃO PODE FORMAR\033[m triângulos!')
