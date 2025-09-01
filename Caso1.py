produtos = []


produto1 = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
produto2 = {"nome": "Feijão", "preco": 9.50, "estoque": 80}
produto3 = {"nome": "Macarrão", "preco": 4.20, "estoque": 150}


produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)


for produto in produtos:
    print(f"O produto {produto['nome']} custa R${produto['preco']} e tem {produto['estoque']} unidades em estoque.")
