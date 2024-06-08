v = int(input('Qual é a velocidade atual do carro? ')) #SISTEMA DE MULTA
if 80 < v:
    multa = (v-80) * 7
    print(f'\033[31mMULTADO! Você excedeu o limite permitido de 80Km/h\033[m')
    print(f'Você deve paga uma multa de R${multa:.2f}!')
else:
    print('Esta dentro do limite permitido nesta via!')
print('\033[33mTenha um bom dia! Dirija com segurança!')
