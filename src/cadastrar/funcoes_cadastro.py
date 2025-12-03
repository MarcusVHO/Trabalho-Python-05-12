import os

from src.pesquisar.pesquisa_funcoes import pesquisar_por_cpf


def verificar_nome():
    nome = input("Digite seu nome: ")
    nome_separado = nome.split(" ")
    if not len(nome_separado) > 1:
        os.system("cls")
        print("O nome deve conter mais de uma palavra!! ")
        print("Digite novamente!! ")
        nome = verificar_nome()
    return nome.upper()

#recursividade!!!


def verificar_cpf(lista_pessoas):
    while True:
        print("Digite seu CPF no formato XXX.XXX.XXX-XX por favor!!!")
        cpf = input("Digite seu CPF: ")
        if not cpf:
            os.system("cls")
            print("CPF digitado invalido!!!!")
            print("Digite novamente!! ")
            continue

        retornado = verificar_formato_cpf(cpf)

        if not retornado:
            os.system("cls")
            print("CPF digitado invalido!!!!")
            print("Digite novamente!! ")
            continue

        cpf_existe = pesquisar_por_cpf(cpf, lista_pessoas)

        if cpf_existe:
            print("Este CPF já está cadastrado!!")
            return None

        return cpf


def verificar_formato_cpf(cpf):
    formato_cpf = cpf.split(".")

    if len(formato_cpf) != 3:
        return False

    ultima_parte = formato_cpf[-1].split("-")

    if len(ultima_parte) != 2:
        return False

    return True

def verificar_formato_nascimento(nascimento):
    formato_nascido = nascimento.split("/")

    if len(formato_nascido) != 3:
        return False
    elif len(formato_nascido[0]) != 2:
        return False
    elif len(formato_nascido[1]) != 2:
        return False
    elif len(formato_nascido[2]) != 4:
        return False
    else:
        return True

def verificar_nascimento():
    nascimento = input("Digite sua data de nascimento (formato: XX/XX/XXXX): ")
    if not nascimento:
        os.system("cls")
        print("Data invalida!!!!!")
        print("Digite novamente!!!")
        nascimento = verificar_nascimento()

    esta_correto = verificar_formato_nascimento(nascimento)
    if not esta_correto:
        os.system("cls")
        print("Data invalida!!!!!")
        print("Digite novamente!!!")
        nascimento = verificar_nascimento()


    return nascimento


def verificar_email():
    email = input("Digite seu email: ")
    return email


def verificar_telefone():
  tamanho_peca = input("Digite o telefone (deve conter 9 numeros): ")
  if len(tamanho_peca) != 9:
      print("Telefone invalido!!!")
      tamanho_peca = verificar_telefone()
  return tamanho_peca

def verificar_naturalidade():
    naturalidade = input("Digite sua naturalidade: ")
    return naturalidade


def verificar_endereco():
    endereco = input("Digite seu endereco: ")
    return endereco


def verificar_numero():
    numero = input("Digite sua numero: ")
    return numero

def verificar_bairro():
    bairro = input("Digite seu bairro: ")
    return bairro


def verificar_cidade():
    cidade = input("Digite sua cidade: ")
    return cidade

def verificar_estado():
    estado = input("Digite seu estado: ")
    return estado

