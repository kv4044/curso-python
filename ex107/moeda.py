def metade(preco):
    met = preco / 2
    return met


def dobro(preco):
    dob = preco * 2
    return dob


def aumento(preco, taxa):
    aum = preco + (preco * taxa / 100)
    return aum


def diminuir(preco, taxa):
    dim = preco - (preco * taxa / 100)
    return dim