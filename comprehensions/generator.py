#generator expression (ainda não é tupla)

gen = (x ** 2 for x in range(6))
print(gen)

#convertendo em tupla
quadrados_tuple = tuple(x ** 2 for x in range(6))
print(quadrados_tuple)

"""
Um generator em Python é um iterador especial que não armazena todos os valores na memória de uma vez, 
mas sim gera cada valor sob demanda. No caso, gen não é uma lista de quadrados de 0 a 5, 
mas um objeto que sabe como calcular esses valores quando você pedir. 
SA grande vantagem é que o generator economiza memória.

"""