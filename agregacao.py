class Chave:
    def __init__(self, status):
        self.status = status
        self.gira = False

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.item = None

    # método para pegar a chave e incluir no atributo item
    def pegar(self, chave:Chave):
        if self.item == None:
            self.item = chave

    def movimenta(self):
        if not self.item.gira:
            self.item.gira = True
            print(f'{self.nome} girou a chave.')
        else:
            print(f'A chave ja foi girada.')

p1 = Pessoa('Bruno', 30)
ch = Chave('Definida')
p1.pegar(ch)
print(p1.item.status)
p1.movimenta()