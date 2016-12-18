from cep import Endereco

recebe = input("Digite seu Cep:")

endereco_consultado = Endereco(cep=recebe)

print(endereco_consultado.rua)
