print('='*15)        #CALCULO DO IMC
print('CALCULO DE IMC')
print('='*15)
kg = float(input('Qual é seu peso? (Kg) '))
m = float(input('Qual sua altura? (m) '))
imc = kg/(m**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if 18.5 > imc:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO!')
