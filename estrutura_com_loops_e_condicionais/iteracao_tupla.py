#tupla de numeros

numeros = (3, 7, 10, 15, 20)

#itera pela tupla e mostra apenas os numeros pares
for n in numeros:
    if n % 2 == 0:
        print(f"{n} é par")
