from random import randint  #ADVINHE O NUMERO
from time import sleep

n = randint(0, 5)  #faz o pc "pensar"

print('-=-' * 15)
print('\033[36mVou pensar em um numero para você adivinhar\033[m')
print('-=-' * 15)

nj = int(input('Digite um numero de 0 a 5: '))  #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)  #faz demorar 1 segundos
if nj == n:
    print('\033[32mVocê acertou o numero que eu pensei, PARABENS!!!\033[m')
else:
    print(f'\033[31mEU GANHEI! Pensei no numero no {n} e não no numero {nj}!')
