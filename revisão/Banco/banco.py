class Banco:
  def __init__(self, nomeDoBanco, agencia):
    self.nomeDoBanco = nomeDoBanco
    self.agencia = agencia
    self.contas = []
    
  def visualizarContas(self):
    print(f'\n--- Contas do banco {self.nomeDoBanco} ---')
    for conta in self.contas:
      print(f"Titular: {conta.nome} | N° da conta: {conta.numeroDaConta} | Saldo: R${conta.saldo:.2f}")