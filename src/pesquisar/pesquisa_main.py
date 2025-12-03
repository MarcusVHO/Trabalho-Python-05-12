from src.pesquisar.pesquisa_funcoes import solicitar_nome, solicitar_cpf


def pesquisa_menu(lista_pessoas):
    print("== Escolha a opção desejada de busca ==")
    print(" [ 1 ] = Nome ")
    print(" [ 2 ] = CPF  ")
    opcao = int(input(" Tipo: "))

    if opcao == 1:
       solicitar_nome(lista_pessoas)

    elif opcao == 2:
        solicitar_cpf(lista_pessoas)

    else:
        print("Opção invalida!!")