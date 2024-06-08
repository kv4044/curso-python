n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n%c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes.')
if tot == 2:
    print('E por isso ele é \033[32mPRIMO!')
else:
    print('E por isso ele \033[31mNÃO É PRIMO!')
