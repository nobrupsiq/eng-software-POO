from banco import Banco
from conta import Conta

itau = Banco('Itau', 1)
nubank = Banco('Nubank', 2)


pessoa1 = Conta('Bruno Pires', 200, 111111, 1, itau)
pessoa2 = Conta('Jessica', 120, 222222, 1, itau)
pessoa3 = Conta('Arthur', 2200, 333333, 2, nubank)
pessoa4 = Conta('Jonas', 671.24, 444444, 2, nubank)

print(pessoa1.transferirTed(pessoa2, 200))

itau.visualizarContas()
nubank.visualizarContas()

print(pessoa1.extrato)
itau.visualizarContas()

print(pessoa1.chequeEspecial(200))
itau.visualizarContas()

print(pessoa1.solicitarEmprestimo(4000, 'Reforma da casa'))

print(pessoa1.extrato)
print(pessoa2.extrato)