v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digeite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
#definir o maior
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
#definir o menor
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print(f'O menor numero digitado foi {menor}')
print(f'O maior numero digitado foi {maior}')
