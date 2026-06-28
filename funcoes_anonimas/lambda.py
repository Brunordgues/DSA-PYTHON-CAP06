# São pequenas funções anônimas definidas com a palavra-chave lambda.

dobro = lambda x: x * 2

#print

print(f"O dobro de 7 é: {dobro(7)}")

"""

O dobro de 7 é: 14
A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).

Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez, dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.

Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.


"""

#Lista de números

numeros = [1, 2, 3, 4, 5]

#lambda que retorna o quadrado de cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados) #[1, 4, 9, 16, 25]

"""
Aqui:

lambda x: x**2 define uma função anônima que calcula o quadrado.

map() aplica essa função a cada elemento da lista.

list() converte o resultado do map (um iterador) de volta para lista.

👉 Também daria para fazer com list comprehension, mas aí não seria lambda.

"""