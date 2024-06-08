n = int(input('Digite um numero: '))
print(f'O dobro de {n} é \033[32m{n*2}\033[m.\n O triplo de {n} é \033[33m{n*3}\033[m.\n A raiz quadrada é \033[34m{pow(n, (1/2)):.4}')
