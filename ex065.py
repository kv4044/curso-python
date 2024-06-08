total = totnum = maior = menor = media = 0
opcao = 'S'
while opcao in 'sS':
    n = int(input('Digite um numero: '))
    totnum += 1
    total += n
    if totnum == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
media = total/totnum
print(f'Você digitou {totnum} numeros e a media foi {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
