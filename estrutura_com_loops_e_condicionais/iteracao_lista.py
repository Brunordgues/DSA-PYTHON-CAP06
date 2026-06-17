#lista de nomes

nomes = ["Rutinha", "Thamiris", "Amanda", "Roberto", "Annaline"]

#itera pela lista e mostra apenas os nomes que começam com 'A'
for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome encontrado com A: {nome}")
