from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}o pessoal nascel? '))
    idade = atual-ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'O total de pessoas que atingiram a maioridade são {maior}.')
print(f'O total de pessoas que nao atigiram a maioridade são {menor}.')
