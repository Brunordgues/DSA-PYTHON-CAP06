produtos = {"arroz": 25, "feijao": 12, "carne": 45, "Macarrão": 8}

#itera pelo dicionario e mostra apenas produtos acima de 20 reais
for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")