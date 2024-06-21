def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')