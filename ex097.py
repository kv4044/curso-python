def escreva(msg):
    tamanho = len(msg) + 4
    print('='*tamanho)
    print(msg.center(tamanho))
    print('='*tamanho)


txt = str(input('Digite uma frase: '))
escreva(txt)
