
def pesquisa_por_nome(nome, lista_pessoas):
    for pessoa in lista_pessoas:
        if pessoa["nome"] == nome.upper():
            return pessoa
    return None


def exibir_bunitim(pessoa):
    print("NOME: ", pessoa["nome"])
    print("CPF: ", pessoa["cpf"])
    print("DATA DE NASCIMENTO: ", pessoa["nascimento"])
    print("EMAIL: ", pessoa["email"])
    print("TELEFONE: ", pessoa["telefone"])
    print("NATURALIDADE: ", pessoa["naturalidade"])
    print("ENDEREÇO:", pessoa["endereco"])
    print("NUMERO: ", pessoa["numero"])
    print("BAIRRO: ", pessoa["bairro"])
    print("CIDADE: ", pessoa["cidade"])
    print("ESTADO: ", pessoa["estado"])



def solicitar_nome(lista_pessoas):
    nome = input("Digite o nome para busca: ")
    pessoa_encontrada = pesquisa_por_nome(nome,lista_pessoas)

    if pessoa_encontrada:
        exibir_bunitim(pessoa_encontrada)
        input("Pressione ENTER para voltar ao menu...")
    else:
        print("Nenhum nome foi encontrado")
        input("Pressione ENTER para voltar ao menu...")





def pesquisar_por_cpf(cpf, lista_pessoas):
    for pessoa in lista_pessoas:
         if pessoa["cpf"] == cpf:
             return pessoa
    return None


def solicitar_cpf(lista_pessoas):
    cpf = input("Digite o CPF para busca (formato: XXX.XXX.XXX-XX): ")
    pessoa_encontrada = pesquisar_por_cpf(cpf, lista_pessoas)

    if pessoa_encontrada:
        exibir_bunitim(pessoa_encontrada)
        input("Pressione ENTER para voltar ao menu...")
    else:
        print("Nenhum Cpf foi encontrado")



















