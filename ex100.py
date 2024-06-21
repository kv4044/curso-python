from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 9)
        print(n, end=' ')
        lista.append(n)
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    pars = 0
    for valor in lista:
        if valor % 2 == 0:
            pars += valor
    print(f'Somando os valores pares de {lista}, temos {pars}')


numeros = list()
sorteia(numeros)
somapar(numeros)
