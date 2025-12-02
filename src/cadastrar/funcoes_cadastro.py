import os

from src.pesquisar.pesquisar import pesquisar_por_cpf


def verificar_nome():
    nome = input("Digite seu nome: ")
    nome_separado = nome.split(" ")
    if not len(nome_separado) > 1:
        os.system("cls")
        print("O nome digitado está incorreto!!! ")
        print("Digite novamente!! ")
        verificar_nome()
    return nome.upper()

#recursividade!!!


def verificar_cpf(lista_pessoas):
    print("Digite seu CPF no formato XXX.XXX.XXX-XX por favor!!!")
    cpf = input("Digite seu CPF: ")
    if not cpf:
        os.system("cls")
        print("CPF digitado invalido!!!!")
        print("Digite novamente!! ")
        verificar_cpf(lista_pessoas)

    retornado = verificar_formato_cpf(cpf)

    if not retornado:
        os.system("cls")
        print("CPF digitado invalido!!!!")
        print("Digite novamente!! ")
        verificar_cpf(lista_pessoas)

    cpf_existe = pesquisar_por_cpf(cpf, lista_pessoas)

    if cpf_existe:
        print("Este CPF já cadastrado")
        return None
    return cpf


def verificar_formato_cpf(cpf):
    formato_cpf = cpf.split(".")

    if len(formato_cpf) != 3:
        return False

    ultima_parte = formato_cpf[-1].split("-")

    if len(ultima_parte) != 2:
        return False
    elif len(ultima_parte[0]) != 3:
        return False
    elif len(ultima_parte[1]) != 2:
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
    nascimento = input("Digite sua data de nascimento: ")
    if not nascimento:
        os.system("cls")
        print("Data invalida!!!!!")
        print("Digite novamente!!!")
        verificar_nascimento()

    esta_correto = verificar_formato_nascimento(nascimento)
    if not esta_correto:
        os.system("cls")
        print("Data invalida!!!!!")
        print("Digite novamente!!!")
        verificar_nascimento()


    return nascimento


def verificar_email():
    email = input("Digite seu email (valido apenas @gmail): ")
    return email


def verificar_telefone():
  tamanho_peça = int(input("Digite o telefone: "))
  if len(tamanho_peça) != 9:
      print("Telefone invalido!!!")
      verificar_telefone()
  return tamanho_peça()

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


verificar_nascimento()
