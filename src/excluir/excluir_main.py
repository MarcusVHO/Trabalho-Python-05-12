from src.pesquisar.pesquisar import pesquisar_por_cpf


def excluir(lista):
    cpf_da_pessoa = input('Digite o CPF da pessoa a ser excluida: ')
    pessoa_a_ser_excluida = pesquisar_por_cpf(cpf_da_pessoa, lista)
    if pessoa_a_ser_excluida:
        lista.remove(pessoa_a_ser_excluida)
        print("pessoa excluida cadastrada com sucesso!")
        input('Pressione ENTER para sair...')
    else:
        print("Nenhuma pessoa encontrada!!!")
        input("Pressione para continuar...")