#argumentos de tamanho variável ()

def dsa_exibe_info_pessoa(**kwargs):

    """Exibe informações como pares chave-valor"""

    print("\nInformações da Pessoa:\n")

    for chave, valor in kwargs.items():
        print(f" - {chave}: {valor}")


dsa_exibe_info_pessoa(nome = "Carla",
                      profissao = "Engenheira de Dados",
                      hobby = "Leitura")

dsa_exibe_info_pessoa(nome = "Bob", profissao = "Cientista de Dados")