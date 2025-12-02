from src.cadastrar.cadastro_main import obter_dados
from src.menus.menu_principal import menu_principal
import os

from src.pesquisar.pesquisar import pesquisa_menu

while True:
    opcao = menu_principal()
    lista_pessoas = []
    match opcao:
        case 1:
           os.system('cls')
           print("============= Cadastro ==============")
           lista_pessoas.append(obter_dados(lista_pessoas))
           print("Pessoa cadastrada com sucesso!")
           input("Pressione ENTER para continuar...")


        case 2:
            os.system('cls')
            print("============= Pesquisa ==============")
            pesquisa_menu(lista_pessoas)
        case 5:
            os.system('cls')
            print("Saindo...")
            break