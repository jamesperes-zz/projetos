from cadastro import Cadastro

nome_recebe = input("Digite o nome do cliente: ")

telefone_recebe = input("Digite o numero de telefone: ")

saldo = 0

tr = "conta"

cadastrando = Cadastro.cadastrar(nome=nome_recebe,telefone=telefone_recebe,
                                 saldo=saldo,tr=tr)
