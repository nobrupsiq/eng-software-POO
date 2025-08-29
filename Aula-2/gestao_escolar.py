class Escola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota1 = None
        self.nota2 = None
        self.nota_final = None

    def apresentar(self):
        print(f"O aluno {self.nome}")

    def nota(self, nota_1, nota_2):
        self.nota1 = nota_1
        self.nota2 = nota_2

    def nota(self, nota_1, nota_2):
        self.nota1 = nota_1
        self.nota2 = nota_2

    def calcular(self):
        self.nota_final = (self.nota1 + self.nota2) / 2

        if self.nota_final >= 7:
            print(f"Aluno {self.nome} aprovado {self.nota_final}!")
        elif self.nota_final < 7 and self.nota_final >= 4:
            print(f"O aluno {self.nome} está em recuperação {self.nota_final}.") 
        else:
            print(f"Aluno {self.nome} Reprovado {self.nota_final}!")
