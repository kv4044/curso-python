from random import randint  #Feito por kaiky
from time import sleep      #JOKENPO

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogada = int(input('Qual é sua jogada? '))
computador = randint(0, 2)
pc = 0
cara = 0
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 12)
#jogador ganha
if jogada == 0 and computador == 2:
    print('Computador jogou \033[1;31mTESOURA\033[m')
    print('Jogador jogou \033[1;32mPEDRA\033[m')
    cara = 1
elif jogada == 1 and computador == 0:
    print('Computador jogou \033[1;31mPEDRA\033[m')
    print('Jogador jogou \033[1;32mPAPEL\033[m')
    cara = 1
elif jogada == 2 and computador == 1:
    print('Computador jogou \033[1;31mPAPEL\033[m')
    print('Jogador jogou \033[1;32mTESOURA\033[m')
    cara = 1
#Computador ganha
elif computador == 0 and jogada == 2:
    print('Computador jogou \033[1;32mPEDRA\033[m')
    print('Jogador jogou \033[1;31mTESOURA\033[m')
    pc = 1
elif computador == 1 and jogada == 0:
    print('Computador jogou \033[1;32mPAPEL\033[m')
    print('Jogador jogou \033[1;31mPEDRA\033[m')
    pc = 1
elif computador == 2 and jogada == 1:
    print('Computador jogou \033[1;32mTESOURA\033[m')
    print('Jogador jogou \033[1;31mPAPEL\033[m')
    pc = 1
print('-=' * 12)
if cara == 1:
    print('\033[32mJOGADOR VENCEU!\033[m')
elif pc == 1:
    print('\033[31mCOMPUTADOR VENCEU!\033[m')
if computador == jogada:
    print('\033[33mEmpate\033[m')
