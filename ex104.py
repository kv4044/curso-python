def leiaint(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO!Digite um numero inteiro valido.\033[m')
        return valor


n = leiaint('Digitem um numero: ')
print(f'Você acabou de digitar o numero {n}')