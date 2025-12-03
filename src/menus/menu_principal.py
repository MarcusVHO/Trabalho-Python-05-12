import os

def menu_principal():
    print("============= Sistema de Cadastro =============")
    print("1 - Cadastrar Pessoa")
    print("2 - Pesquisar Pessoa")
    print("3 - Excluir Pessoa")
    print("4 - Atualizar Cadastro")
    print("5 - Listar Pessoas")
    print("6 - Sair do sistema")
    print("===============================================")

    opcao = int(input("Digite a opção desejada: "))
    if opcao < 0 or opcao > 6:
        os.system('cls')
        print("!!!OPÇÃO INVALIDA!!!")
        menu_principal()

    return opcao