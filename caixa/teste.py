from cliente import Cliente
from contas import Conta
joao=Cliente("joao da silva", "777-1234")
maria=Cliente("maria da silva", "555-4321")
jose=Cliente("jose da silva", "123456")


conta1=Conta([joao],1, 1000)
conta2=Conta([maria, joao], 2 , 500)
conta3=Conta([jose],3, 100)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta3.saque(200)
conta1.extrato()
conta2.extrato()
