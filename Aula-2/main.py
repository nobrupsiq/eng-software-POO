from produto import Produto as prod
from gestao_escolar import Escola as scho

produto1 = prod("Leite", 20.00, 40)
produto2 = prod("Maça", 9.99, 30)
produto3 = prod("Água", 3.99, 50)

aluno1 = scho('Zé da manga', 25)
aluno2 = scho('Zé das Coves', 30)
aluno3 = scho('Maria da Manga', 45)

listaP = [produto1, produto2, produto3]
listaA = [aluno1, aluno2, aluno3]

for i in range(3):
    listaP[i].apresentacao(), print('Comprou'), listaA[i].apresentar(), print('apresentacao')