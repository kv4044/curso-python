def notas(*num, sit=False):
    """
    -> Função para analizar notas e situações de varios alunos.
    :param num: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    tudo = {}
    print(num)
    cont = maior = menor = numeros = 0
    situacao = ' '
    tudo['total'] = len(num)
    tudo['maior'] = max(num)
    tudo['menor'] = min(num)
    tudo['media'] = sum(num)/len(num)
    if sit:
        if tudo['media'] >= 7:
            tudo['situação'] = 'BOA'
        elif tudo['media'] >= 5:
            tudo['situação'] = 'RAZOAVEL'
        else:
            tudo['situacao'] = 'RUIM'
    return tudo

help(notas)
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
