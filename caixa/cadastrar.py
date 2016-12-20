from cadastro import Cadastro

nome_recebe = input("Digite o nome do cliente: ")

telefone_recebe = input("Digite o numero de telefone: ")

cadastrando = Cadastro.cadastrar(nome=nome_recebe,telefone=telefone_recebe)
