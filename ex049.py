print('-='*15)
print('\033[1;31mTABUADA V2.0\033[m')
print('-='*15)
n = int(input('Digite um nuemro para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print(f'{n} x {c:2} = {n*c}')
print('-'*12)
