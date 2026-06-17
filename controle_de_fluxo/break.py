#lista de numeros

numeros = [1,2,3,4,5,6,7,8,9,10]

#mensagem
print("\nBuscando pelo número 5...")

#loop com break
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado!!")
        break #sai do loop
    print(f"Verificando {numero}...")