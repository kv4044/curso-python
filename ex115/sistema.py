from ex115 .lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # opção de listar o conteudo de um arquivo.
        lerarquivo(arq)
    elif resp == 2:
        # opção de casdastrar uma nova pessoal.
        cabecalho('NOVO CADASTROO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # opção de sair do sistema.
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        # digitou opção errada.
        print('\033[31mERRO! Digite uma opção valida!\033[m')
    sleep(1)
