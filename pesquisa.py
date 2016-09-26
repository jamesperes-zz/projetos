# coding: utf-8

from unicodedata import normalize

#colocar data
from datetime import datetime
now = datetime.now()

print ( 30 * '-')
print (" \n    Pesquisa de nomes     \n")
print (30 * '-')



arq = input(str("\ndigite o nome do arquivo: "))
palavra_in = input(str("Digite a palavra a ser contada: "))
print()


# retirar a acentuacao  // codigo de github.com/etandel //
def remove_diacritic(s):
	return (normalize('NFKD', s)
			.encode('ascii', 'ignore')
			.decode('ascii'))

arq = arq + ".txt"

f = open(arq, 'r', encoding="utf-8")
content = f.read()
palavra = (remove_diacritic(content)).lower().split()


print(palavra.count(palavra_in))


# Grava um historico das pesquisas feitas
arquivo = open('teste_de_hist.txt', 'r')
conteudo = arquivo.readlines()

conteudo.append('\n\nLivro lido: %s'%arq)
conteudo.append('\nPalavra procurada: %s'%palavra_in)
conteudo.append('\nVezes encontrada: %s'%(palavra.count(palavra_in)))
conteudo.append('\nPesquisado em: %s/%s/%s'%(now.day, now.month, now.year))


arquivo = open('teste_de_hist.txt', 'w')
arquivo.writelines(conteudo)


stop = input("\n\nDigite Enter para sair... ")
