def voto(ano):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[31mVOTO NEGADO.\033[m'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: \33[32mVOTO OBRIGATÓRIO.\033[m'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: \033[33mVOTO OPCIONAL.\033[m'


anonasc = int(input('Em que ano você nasceu?'))
print(voto(anonasc))
