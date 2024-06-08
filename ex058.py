from random import randint
tentativa = 1
computador = randint(0, 10)
print('-=-'*16)
print('\033[35mVou pensar em um numero pra você advinhar v2.0\033[m')
print('-=-'*16)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinha qual foi?')
jogador = int(input('Qual é seu palpite? '))
while jogador != computador:
    if jogador > computador:
        print('\033[34mMenos\033[m... Tente outra vez.')
        jogador = int(input('Qual seu paltpite? '))
        tentativa += 1
    else:
        print('\033[31mMais\033[m... Tente outra vez.')
        jogador = int(input('Qual seu palpite?'))
        tentativa += 1
print(f'Acertou com {tentativa} tentativas. \033[32mPARABÉNS!\033[m')
