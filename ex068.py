from random import randint

print('=-'*14)
print('\033[35mVAMOS JOGAR PAR OU ÍMPAR\033[m')
v = 0
while True:
    print('=-' * 14)
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    print('-'*28)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end=' ')
    print('DEU \033[34mPAR\033[m' if soma % 2 == 0 else 'DEU \033[33mIMPAR\033[m')
    print('-'*28)
    if parouimpar == 'P':  # se jogar par
        if soma % 2 == 0:  # vence
            v += 1
            print('\033[32mVocê VENCEU!\033[m')
        else:              # perde
            break
    elif parouimpar == 'I':  # se jogar impar
        if soma % 2 == 1:  # vence
            v += 1
            print('\033[32mVocê VENCEU!\033[m')
        else:              # perde
            break
    print('Vamos jogar novamente...')
print('\033[31mVocê PERDEU!\033[m')
print('-='*14)
print(f'GAME OVER! Você venceu {v} vezes.')
