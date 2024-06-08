n = int(input('Me diga um numero qualquer: ')) #IMPAR OU PAR
resultado = n % 2
if resultado == 0:
    print(f'O numero \033[32m{n} é PAR')
else:
    print(f'O numero \033[31m{n} é IMPAR')
