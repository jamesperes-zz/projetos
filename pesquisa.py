# coding: utf-8

from unicodedata import normalize

arq = input(str("digite o nome do arquivo: "))
palavra_in = input(str("Digite a palavra a ser contada: "))


# retirar a acentuacao
def remove_diacritic(s):
	return (normalize('NFKD', s)
			.encode('ascii', 'ignore')
			.decode('ascii'))

arq = arq + ".txt"

f = open(arq, 'r', encoding="utf-8")

content = f.read()


palavra = (remove_diacritic(content)).lower().split()

print(palavra.count(palavra_in))
