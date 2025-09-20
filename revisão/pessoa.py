# 1 - Crie uma class que reserve os atributos de uma pessoa
class Pessoa:
  def __init__(self, nome, idade, altura, sexo, corDoCabelo):
    self.nome = nome
    self.idade = idade
    self.altura = altura
    self.sexo = sexo
    self.corDoCabelo = corDoCabelo
    
pessoa1 = Pessoa("João", 25, 1.75, "Masculino", "Preto")
pessoa2 = Pessoa("Maria", 30, 1.65, "Feminino", "Loiro")