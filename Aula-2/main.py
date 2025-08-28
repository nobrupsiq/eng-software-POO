from produto import Produto as prod

produto1 = prod("Leite", 20.00, 40)
produto2 = prod("Maça", 9.99, 30)
produto3 = prod("Água", 3.99, 50)

for i in [produto1, produto2, produto3]:
    i.apresentacao()