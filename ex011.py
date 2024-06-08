largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua area é de {area}m2')
print(f'Para pintar essa parede, você precisará de {area/2}l de tinta.')