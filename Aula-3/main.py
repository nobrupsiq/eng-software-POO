from Car import Chave
from Car import Carro

ch = Chave("FIAT")
ch1 = Chave("Chevrolet")

car1 = Carro("Uno", 1998, 'Verde', 1.0, "ABC-1234", ch)
car1.abrirCarro(ch)

car1.ligar_carro()

for i in range(5):
    car1.acelerar()


# O carro tem que desligar, mas não pode desligar acelerado
# tem que ter um método para frear de 5 em 5
# e tem que ter a inserção da ativação da chave assim que o metodo abrir for True