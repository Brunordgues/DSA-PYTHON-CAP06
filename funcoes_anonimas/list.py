"""
Aqui:

lambda x: x**2 define uma função anônima que calcula o quadrado.

map() aplica essa função a cada elemento da lista.

list() converte o resultado do map (um iterador) de volta para lista.

👉 Também daria para fazer com list comprehension, mas aí não seria lambda.

"""

#lista de numeros

numeros = [1, 2, 3, 4, 5, 6]

#primeiro calculamos os quadrados com map + lambda

quadrados = list(map(lambda x: x ** 2, numeros))

#agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

# Atual (funciona, mas com dois pontos extras)
print(f"quadrados:", quadrados)  # Saída: quadrados: [1, 4, 9, 16, 25, 36]

# Mais limpo:
print(f"quadrados: {quadrados}")  # Saída: quadrados: [1, 4, 9, 16, 25, 36]