from src.atualizar.atualizar_main import atualizar_pessoa
from src.cadastrar.cadastro_main import obter_dados
from src.excluir.excluir_main import excluir
from src.menus.menu_principal import menu_principal
import os

from src.pesquisar.pesquisa_main import pesquisa_menu
from src.pesquisar.pesquisa_funcoes import exibir_bunitim


lista_pessoas = []
while True:
    os.system("cls")
    opcao = menu_principal()
    match opcao:
        case 1:
           os.system('cls')
           print("============= Cadastro ==============")
           pessoa = obter_dados(lista_pessoas)
           exibir_bunitim(pessoa)
           lista_pessoas.append(pessoa)
           print("Pessoa cadastrada com sucesso!")
           input("Pressione ENTER para continuar...")


        case 2:
            os.system('cls')
            print("============= Pesquisa ==============")
            pesquisa_menu(lista_pessoas)

        case 3:
            os.system('cls')
            excluir(lista_pessoas)

        case 4:
            os.system('cls')
            atualizar_pessoa(lista_pessoas)

        case 5:
            os.system('cls')
            for pessoa in lista_pessoas:
                print(" ")
                print("="*20)
                exibir_bunitim(pessoa)
                print("=" * 20)
                print(" ")
            input("Pressione ENTER para continuar...")

        case 6:
            os.system('cls')
            print("Saindo...")
            break