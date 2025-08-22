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

    def calcular(self):
        self.nota_final = (self.nota1 + self.nota2) / 2
    
        variavel = ''

        if self.nota_final >= 7:
            variavel = f"Aluno {self.nome} aprovado {self.nota_final}!"
        elif self.nota_final < 7 and self.nota_final >= 4:
            variavel = f"O aluno {self.nome} está em recuperação {self.nota_final}."
        else:
            variavel = f"Aluno {self.nome} Reprovado {self.nota_final}!"

        return variavel

aluno = Escola()
aluno.inscricao()
aluno.nota()
print(aluno.calcular())