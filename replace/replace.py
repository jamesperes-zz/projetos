# importa requisitos
import glob
from names import nomes_retirar
import re


def replaced(retirar):

    # listar todos txt
    todos_arqs = glob.glob('./**/*.txt', recursive=True)

    for nome_do_arq_da_vez in todos_arqs:
        print(nome_do_arq_da_vez)

        obj_arquivo_aberto = open(nome_do_arq_da_vez, 'r')

        lista_de_linhas = obj_arquivo_aberto.read()

        for palavra, troca in retirar.items():

            if palavra in lista_de_linhas:
                pa = str(palavra)
                tr = str(troca)
                lista_de_linhas = re.sub(pa, tr, lista_de_linhas)

        #print(lista_de_linhas)
        novo_arquivo = open(nome_do_arq_da_vez, 'w')
        novo_arquivo.write(lista_de_linhas)
    return lista_de_linhas


if __name__ == '__main__':
    retirar = nomes_retirar
    retorno_pesquisa = replaced(retirar)
