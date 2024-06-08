tupla = ('aprender', 'programar', 'linguangem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
