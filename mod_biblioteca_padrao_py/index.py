# Usando o módulo 'math' para funções matemáticas
import math

# Usando o módulo "RANDOM" para gerar números aleatórios
import random

#calculan a raiz quadrada
raiz_quadrada = math.sqrt(25)
print(f"a raiz de 25 é: {raiz_quadrada}")

# Gera um inteiro entre 1 e 100
numero_aleatorio = random.randint(1, 100) 
print(f"Um número aleatório entre 1 e 100: {numero_aleatorio}")

# Seleciona aleatoriamente uma cidade da lista
cidade_aleatoria = random.choice(["Rio de Janeiro", "Salvador", "Curitiba"])
print(f"Cidade escolhida aleatoriamente: {cidade_aleatoria}")