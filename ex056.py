nvelho = ''
ivelho = 0
totm = 0
totidade = 0
for n in range(1, 5):
    print(f'----- {n} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totidade += idade
    if sexo in 'Mm' and idade > ivelho:
        nvelho = nome
        ivelho = idade
    if sexo in 'Ff' and idade < 20:
        totm += 1
media = totidade / 4
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho tem {ivelho} anos e se chama {nvelho}.')
print(f'Ao todo são {totm} mulheres com menos de 20 anos.')
