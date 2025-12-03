from src.cadastrar.cadastro_main import obter_dados
from src.pesquisar.pesquisa_funcoes import pesquisar_por_cpf


def atualizar_pessoa(lista):
    cpf = input("Digite o CPF para atualizar: ")
    pessoa_a_ser_atulizada = pesquisar_por_cpf(cpf, lista)
    if pessoa_a_ser_atulizada:
        index = lista.index(pessoa_a_ser_atulizada)
        pessoa_atulizada = obter_dados(lista)

        lista[index] = pessoa_atulizada
        print("pessoa atulizada com sucesso!")
        input('Pressione ENTER para sair...')
    else:
        print("Nenhuma pessoa encontrada!!!")
        input('Pressione ENTER para sair...')