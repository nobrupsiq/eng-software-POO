class Escola:
    def __init__(self, nome="", idade=0, nota1=0.0, nota2=0.0):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota_final = None

    def inscricao(self):
        self.nome = input("Nome do aluno: ")
        self.idade = int(input(f"Idade do {self.nome}: "))

    def nota(self):
        nota1 = float(input('N1: '))
        nota2 = float(input('N2: '))
        self.nota1 = nota1
        self.nota2 = nota2

    def calculo(self):
        self.nota_final = (self.nota1 + self.nota2) / 2

        if self.nota_final >= 7:
            print(f"Aluno {self.nome} aprovado.")
        elif self.nota_final < 7 and self.nota_final >= 4:
            print(f"O aluno {self.nome} está em recuperação.")
        else:
            print(f"Aluno {self.nome} Reprovado!")

ze = Escola()
ze.inscricao()
print(ze.nome)
