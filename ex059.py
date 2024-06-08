from time import sleep
escolha = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segndo valor: '))
while escolha != 5:
    print('=-='*10)
    print('''Escolha sua opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR ''')
    escolha = int(input('Sua opção: '))
    print('=-='*10)
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre \033[31m{n1} + {n2}\033[m é \033[32m{soma}\033[m')
    elif escolha == 2:
        mult = n1 * n2
        print(f'O resultado entre \033[31m{n1} x {n2}\033[m é \033[32m{mult}\033[m')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero entre {n1} e {n2} foi \033[32m{maior}\033[m')
    elif escolha == 4:
        print('Quais são os novos numeros?  ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('')
    else:
        print('\033[31mTem esse numero no menu?\033[m')
    sleep(1)
print('\033[31mSaindo...')
