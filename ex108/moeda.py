def metade(preco=0):
    met = preco / 2
    return met


def dobro(preco=0):
    dob = preco * 2
    return dob


def aumento(preco=0, taxa=0):
    aum = preco + (preco * taxa / 100)
    return aum


def diminuir(preco=0, taxa=0):
    dim = preco - (preco * taxa / 100)
    return dim


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

