print('-='*15)
print('\033[1;31mTABUADA V3.0\033[m')
print('-='*15)
while True:
    n = int(input('Quer saber a tabuadade qual número? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
        c += 1
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
