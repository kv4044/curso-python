def metade(preco=0, formato=False):
    """

    :param preco: O preço do produto.
    :param formato: Formata para (exemplo):R$100,00.
    :return: Retorna a metade do preço.
    """
    res = preco / 2
    return res if format is False else moeda(res)


def dobro(preco=0, formato=False):
    """

    :param preco: O preço do produto.
    :param formato: Formata para (exemplo):R$100,00.
    :return: Retorna o dobro do preço.
    """
    res = preco * 2
    return res if format is False else moeda(res)


def aumento(preco=0, taxa=0, formato=False):
    """

    :param preco: O preço do produto.
    :param taxa: Taxa é um aumento no preço.
    :param formato: Formata para (exemplo):R$100,00.
    :return: Retorna um aumento no preço de tantos %.
    """
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """

    :param preco: O preço do produto.
    :param taxa: Taxa é uma diminuição no preço.
    :param formato: Formata para (exemplo):R$100,00.
    :return: Retorna um desconto no preço de tantos %.
    """
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """

    :param preco: O preço do produto.
    :param moeda: O tipo de moeda.
    :return: Retorna um Formato (exemplo):R$100,00.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')
