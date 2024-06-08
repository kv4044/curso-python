cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quize', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        n = int(input(' Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente.', end='')
    print(F'Você digitou o numero {cont[n]}')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('Fim')
