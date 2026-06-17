#criando um dicionário com o número de cursos em formações da DSA
formacoes_dsa = {"Formação em CCientista de Dados": 6, "Formação em Analista de Dados": 4, "Formação em Engenheiro de Dados": 5}

#loop for percorrendo o dicionário
for chave, valor in formacoes_dsa.items():
    print(chave, ":", valor)