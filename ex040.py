n1 = float(input('Priemira nota: '))  #SISTEMAS DE NOTAS ALUNOS
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m:.1f}.')
if m < 5:
    print('O aluno está \033[4:31mREPROVADO!\033[m')
elif 5 <= m < 7:
    print('O  aluno esta em \033[4;33mRECUPERAÇÃO!\033[m')
elif m >= 7:
    print('O aluno esta \033[4;32mAPROVADO!\033[m')
