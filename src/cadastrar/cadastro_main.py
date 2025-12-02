


def obter_dados():
    nome = verificar_nome()
    cpf = verificar_cpf()
    email = input("E-mail: ")
    endereco = input("Endereço (rua, avenida etc.): ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    estado = input("Estado: ")
    nascimento = input("Nascimento: ")

    return {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "endereco": endereco,
        "numero": numero,
        "bairro": bairro,
        "estado": estado,
        "nascimento": nascimento
    }




obter_dados()
