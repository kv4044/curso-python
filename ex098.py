from time import sleep


def contagem(i, f, p):
    print('=-'*30)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(1)
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += p
            sleep(0.3)
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= p
            sleep(0.3)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-'*30)
print('Agora é sua vez de personalizar a contagem ')
ini = int(input('Inicio: '))
fim = int(input('FIM:    '))
pus = abs(int(input('Passo:  ')))
contagem(ini, fim, pus)