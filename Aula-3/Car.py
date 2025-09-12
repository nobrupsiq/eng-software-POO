# Definição da classe Chave
class Chave:
    # Método construtor
    def __init__(self, marca):
        self.marca = marca
        self.ativa = False

# Define a classe
class Carro:
    def __init__(self, modelo, ano, cor, potencia, placa, chave:Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = 0

    # Métodos | Ação realizada pela classe
    def abrirCarro(self, chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            self.chave.ativa = True
            print("Carro Aberto")
        else:
            print("O carro já está aberto ou ligado, ou a chave está errada!")

    def ligar_carro(self):
        if not self.ligado and self.aberto:
            self.ligado = True
            print("Carro Ligado")
        else:
            print("O carro já está ligado ou fechado!")

    def acelerar(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro está desligado... Precisa ligar o carro primeiro!")


    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print(f"Freando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro já está parado.")

    def desligar_carro(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("Carro Desligado")
        elif self.velocidade > 0:
            print("Não é possível desligar o carro enquanto ele está em movimento!")
        else:
            print("O carro já está desligado.")
