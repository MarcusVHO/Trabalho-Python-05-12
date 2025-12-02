
def pesquisa_por_nome(nome, lista_pessoas):
    for pessoa in lista_pessoas:
        if pessoa["nome"] == nome.upper():
            return pessoa
    return None



def exibir_bunitim(pessoa):
    print(" ========= RESULTADO ========= ")
    print("NOME: ", pessoa["nome"])
    print("CPF: ", pessoa["cpf"])
    print("EMAIL: ", pessoa["email"])
    print("ENDEREÇO:", pessoa["endereco"])
    print("NUMERO: ", pessoa["numero"])
    print("BAIRRO: ", pessoa["bairro"])
    print("ESTADO: ", pessoa["estado"])
    print("DATA DE NASCIMENTO: ", pessoa["nascimento"])



def solicitar_nome(lista_pessoas):
    nome = input("Digite o nome para busca: ")
    pessoa_encontrada = pesquisa_por_nome(nome,lista_pessoas)

    if pessoa_encontrada:
        exibir_bunitim(pessoa_encontrada)
    else:
        print("Nenhum nome foi encontrado")
        input("Pressione ENTER para voltar ao menu...")


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


def pesquisar_por_cpf(cpf, lista_pessoas):
    for pessoa in lista_pessoas:
         if pessoa["cpf"] == cpf:
             return pessoa
    return None


def solicitar_cpf(lista_pessoas):
    cpf = input("Digite o CPF para busca: ")
    pessoa_encontrada = pesquisar_por_cpf(cpf, lista_pessoas)

    if pessoa_encontrada:
        exibir_bunitim(pessoa_encontrada)
    else:
        print("Nenhum Cpf foi encontrado")



















