from random import randint
from time import sleep

jogos1 = dict()
c = 1
print('Valores sorteados: ')
for cont in range(1, 5):
    dado = randint(1, 6)
    jogos1['jogador' + str(cont)] = dado
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print('=-' * 30)
print(f'{"== RANKING DOS JOGADORES ==".center(20)}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'    {c}º: {k} com {v}.')
    c += 1
    sleep(0.5)
print('='*27)