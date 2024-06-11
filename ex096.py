def area(larg, comp):
    a = l*c
    print(f'A área de um terreno de {larg:.1f}x{comp:.1f} é de {a:.1f}m².')


# Programa Principal
print('Controle de Terrenos ')
print('-'*15)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
