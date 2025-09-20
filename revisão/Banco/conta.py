from banco import Banco

class Conta:
  def __init__(self, nome, saldo, numeroDaConta, agencia, banco: Banco):
    self.nome = nome
    self.saldo = saldo
    self.numeroDaConta = numeroDaConta
    self.agencia = agencia
    self.banco = banco
    self.extrato = []
    self.comprasNoCredito = []
    banco.contas.append(self)
    
  def sacarDinheiro(self, valor):
    if valor <= 0:
      raise ValueError('Valor inválido!')
    if self.saldo < valor:
      raise ValueError('Saldo insuficiente!')
    
    saldoRetirado = valor
    self.saldo -= saldoRetirado
    
    self.extrato.append({'Tipo': 'Saque', 'Valor': saldoRetirado})
    
    return saldoRetirado
  
  def transferirTed(self, destino, valor):
    if valor <= 0:
      raise ValueError('Valor inválido')
    if self.saldo < valor:
      raise ValueError('Saldo insuficiente!')
    
    taxa = 0
    if self.banco.nomeDoBanco != destino.banco.nomeDoBanco:
      taxa = valor * 0.01
      
    total = valor + taxa
    
    if self.saldo < total:
      raise ValueError('Saldo insuficiente!')
    
    self.saldo -= total
    self.extrato.append({
      "tipo": "TED Envio",
      "nome": destino.nome,
      "conta": destino.numeroDaConta,
      "valor": -valor,
      "taxa": taxa,
    })
    
    destino.saldo += valor
    destino.extrato.append({
      "tipo": "TED Recebido",
      "nome": self.nome,
      "conta": self.numeroDaConta,
      "valor": valor
    })
    
    print(f"TED de R${valor:.2f} realizado para {destino.nome} "
          f"(Taxa: R${taxa:.2f})")
    
    return valor

  def transferirPix(self, valor):
    if valor <= 0:
      raise ValueError('Valor inválido!')
    if self.saldo < valor:
      raise ValueError('Saldo insuficiente!')
    
    saldoRetirado = valor
    self.saldo -= saldoRetirado
    
    self.extrato.append({'Tipo': 'Pix', 'Valor': saldoRetirado})
    
    return saldoRetirado
  
  def chequeEspecial(self, valor):
    if valor <= 0:
      raise ValueError('Valor inválido!')
    if self.saldo <= 0:
      saldoRetirado = valor
      self.saldo -= saldoRetirado
      
      self.saldo *= 1.12

      self.extrato.append({
        'Tipo': 'Cheque Especial', 
        'Valor': saldoRetirado, 
        'Saldo final': f'{self.saldo:.2f}'
        })
      
      return saldoRetirado 
    else:
      raise ValueError('Você possui saldo em sua conta!')
    
  def solicitarEmprestimo(self, valor, finalidade):
    if valor < 0:
      raise ValueError('Valor inválido!')
    if not finalidade:
      raise ValueError('Precisa ter uma finalidade!')
    
    dadosDoPedido = {
      'cliente': self.nome,
      'valor': valor,
      'finalidade': finalidade,
      'banco': self.banco.nomeDoBanco,
      'status': 'Em análise'
    }
    
    self.extrato.append({'Tipo': 'Pedido de Empréstimo', 'Dados': dadosDoPedido})
    
    return dadosDoPedido
  
  def usarCredito(self, nomeDoProduto, valorDaCompra):
    if valorDaCompra <= 0:
      raise ValueError('Valor da compra inválido!')
    
    compra = {
      'item': nomeDoProduto,
      'valor': valorDaCompra
    }
    
    self.comprasNoCredito.append(compra)
    self.extrato.append({
      'tipo': 'Crédito',
      'item': nomeDoProduto,
      'valor': valorDaCompra
    })
    print(f"\nCompra no crédito aprovada!\nItem: {nomeDoProduto}\nValor: R${valorDaCompra}")
    
    return compra
  
  def gerarFaturaDeCredito(self):
    totalDaFatura = 0
    print('--- Fatura do cartão de crédito ---')
    for index, item in enumerate(self.comprasNoCredito):
      print(f"{index + 1}. {item['item']} - R${item['valor']:.2f}")
      totalDaFatura += item['valor']
    
    print(f'\nTotal da fatura: R${totalDaFatura:.2f}')