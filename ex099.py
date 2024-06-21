from time import sleep


def maior(*num):
    print('=-'*30)
    print('Analizando valores passados...')
    mais = 0
    for pos, n in enumerate(num):
        print(f'\033[34m{n}\033[m', end=' ')
        sleep(0.3)
        if pos == 0:
            mais = n
        else:
            if n > mais:
                mais = n
    print(f'Foram informados \033[35m{len(num)}\033[m numeros ')
    print(f'O maior valor digitado foi \033[32m{mais}.\033[m')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('=-'*30)
