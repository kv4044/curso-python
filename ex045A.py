from random import randint  #FEITO POR GUANABARA
from time import sleep      #JOKENPO

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 1)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:  #COMPUTADOR JOGA PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[4;31mJOGADA INVÁLIDA!\033[m')
elif computador == 1:  #COMPUTADOR JOGA PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCE!\033[m')
    else:
        print('\033[4;31mJOGADA INVÁLIDA!\033[m')
elif computador == 2:  #COMPUTADOR JOGA TESOURA
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE!\033[m')
    else:
        print('\033[4;31mJOGADA INVÁLIDA!\033[m')
