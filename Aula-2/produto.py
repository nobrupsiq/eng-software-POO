class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Método de apresentação
    def apresentacao(self):
        print(f"Produto: {self.nome} | preço R${self.preco} | Quantidade: {self.quantidade}")

leite = Produto('Leite', 7.99, 10)
maca = Produto('Maça', 0.99, 15)
agua = Produto('Água', 1.99, 20)
