#argumentos de tamanho variavél ()

def dsa_soma_numeros(*args):


     """Soma um número variável de argumentos."""

     total = 0

     for numero in args:
          
          total += numero

     return total

print(f"Soma dos números: {dsa_soma_numeros(1, 2, 3, 4, 5)}")
print(f"Soma dos números: {dsa_soma_numeros(1, 2, 3)}")
print(f"Soma dos numeros: {dsa_soma_numeros(10, 400, 0.3, 120)}")