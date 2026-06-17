#criando uma lista de quadrados dos números de 0 a 9:

quadrados = [x ** 2 for x in range(10)]

#print
print(f"nQuadrados de 0 a 9: {quadrados}")

print(f"\n--------------------------------------------------------------------------------\n")

#criando uma lista de numeros pares de 0 a 20
pares = [x for x in range (21) if x % 2 == 0]

#print
print(f"Números pares de 0 a 20: {pares}")