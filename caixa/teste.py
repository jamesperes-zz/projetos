

from cliente import Cliente
from contas import Conta, Ler


cliente_joao=Cliente("joao da silva", "777-1234")
cliente_maria=Cliente("maria da silva", "555-4321")
cliente_jose=Cliente("jose da silva", "123456")


conta_joao=Conta(cliente_joao,1, 1000)
conta_maria=Conta(cliente_maria, 2 , 500)
conta_jose=Conta(cliente_jose,3, 100)

conta_joao.saque(50)
conta_joao.saque(190)
conta_joao.extrato()


conta_maria.deposito(300)
conta_maria.deposito(95.15)
conta_maria.saque(250)
conta_maria.extrato()

conta_jose.saque(200)
conta_jose.extrato()


teste = 1
imprimir_cliente(teste)
