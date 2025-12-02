from src.cadastrar.funcoes_cadastro import verificar_nome, verificar_cpf, verificar_email, verificar_endereco, \
    verificar_numero, verificar_bairro, verificar_estado, verificar_nascimento, verificar_telefone, \
    verificar_naturalidade, verificar_cidade


def obter_dados(lista_pessoas):
    nome = verificar_nome()
    cpf = verificar_cpf(lista_pessoas)
    if not cpf:
        obter_dados(lista_pessoas)
    nascimento = verificar_nascimento()
    email = verificar_email()
    telefone = verificar_telefone()
    naturalidade = verificar_naturalidade()
    endereco = verificar_endereco()
    numero = verificar_numero()
    bairro = verificar_bairro()
    cidade = verificar_cidade()
    estado = verificar_estado()

    return {
        "nome": nome,
        "cpf": cpf,
        "nascimento": nascimento,
        "email": email,
        "telefone": telefone,
        "naturalidade": naturalidade,
        "endereco": endereco,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
    }

