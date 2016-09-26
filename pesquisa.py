# coding: utf-8

from unicodedata import normalize

arq = input(str("digite o nome do arquivo: "))
palavra_in = input(str("Digite a palavra a ser contada: "))


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

arquivo = open('teste_de_hist.txt', 'w')
arquivo.writelines(conteudo)
