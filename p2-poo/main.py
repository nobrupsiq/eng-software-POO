class Funcionario:
    def __init__(self, nome: str, salario: float):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.nome = nome
        self.salario = salario

    def descrever(self):
        print(f"Funcionário: {self.nome} | Salário: R$ {self.salario:.2f}")

    def calcular_bonus(self):
        return self.salario * 0.05

class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)
        self.equipe = []

    def adicionar_membro(self, nome_membro: str):
        self.equipe.append(nome_membro)

    def calcular_bonus(self):
        return self.salario * 0.10

    def descrever(self):
        print(f"Gerente: {self.nome} | Salário: R$ {self.salario:.2f} | "
              f"Equipe: {len(self.equipe)} membro(s)")

class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, salario: float, linguagem: str):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def calcular_bonus(self):
        return self.salario * 0.08

    def descrever(self):
        print(f"Desenvolvedor: {self.nome} | Salário: R$ {self.salario:.2f} | "
              f"Linguagem: {self.linguagem}")

def imprimir_resumo(funcionario: Funcionario):
    funcionario.descrever()
    print(f"Bônus: R$ {funcionario.calcular_bonus():.2f}")
    print("-" * 40)

if __name__ == "__main__":
    gerente = Gerente("Carlos", 10000)
    dev = Desenvolvedor("Bruno", 8000, "Python")

    gerente.descrever()
    dev.descrever()

    print(f"Bônus do gerente: R$ {gerente.calcular_bonus():.2f}")
    print(f"Bônus do desenvolvedor: R$ {dev.calcular_bonus():.2f}")

    gerente.adicionar_membro("Ana")
    gerente.adicionar_membro("João")

    print("\nApós adicionar membros à equipe:")
    gerente.descrever()

    print("\nResumo de funcionários:")
    imprimir_resumo(gerente)
    imprimir_resumo(dev)
