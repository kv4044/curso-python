r1 = int(input('Primeiro segmento: '))  #SE FORMA UM TRIANGULO E QUAL
r2 = int(input('Segundo segmEneto: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[1;33mEQUILÂTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print(' \033[1;35mESCALENO!\033[m')
    else:
        print(' \033[1;34mISÓSCELES!\033[m')
else:
    print('Os segmentos a cima \033[31mNÃO PODEM FORMAR\033[m triângulos!')
