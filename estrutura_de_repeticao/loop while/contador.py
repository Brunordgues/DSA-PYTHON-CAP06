"""O LOOP WHILE EXECUTA UM BLOCO DE CÓDIGO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA"""

#define a variavel 
contador = 5

#imprime a mensagem
print("Contagem regressiva: ")

#loop
while contador > 0:
    print(contador)
    contador -= 1

#Define a variavel
contador = 0

#imprime a mensagem
print("Contagem regressiva")

#loop
while contador > 1:
    print(contador)
    contador -= 1

# CUIDADO - LOOP INFINITO - PODE TRAVAR O JUPYTER OU MESMO SUA MÁQUINA
# Define a variável
#contador = 2

# Imprime a mensagem
#print("\nContagem regressiva:")

# Loop
#while contador > 1:
    #print(contador)
    #contador -= 1

"""

O for em Python é usado quando você já sabe sobre o que quer iterar (como uma lista, tupla, dicionário, string, range, etc.). Ele percorre cada elemento de uma sequência ou iterável de forma automática, sem que você precise gerenciar manualmente a condição de parada.

Já o while é usado quando você não sabe previamente quantas vezes o loop vai rodar e a repetição depende de uma condição booleana que deve continuar verdadeira para que o loop prossiga. Você precisa cuidar manualmente de alterar o estado dessa condição para evitar loops infinitos.

Em resumo:

for → ideal quando você já tem uma coleção ou um número definido de repetições.

while → ideal quando a repetição depende de uma condição que pode mudar dinamicamente ao longo da execução.

"""