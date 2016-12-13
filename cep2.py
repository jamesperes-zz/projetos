import urllib.request


cep_busca   = input('Digite o CEP: ')
url  = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + cep_busca + "&formato=query_string"

pagina  = urllib.request.urlopen(url)
conteudo = str(pagina.read()).replace("&", " ")
conteudo3  = conteudo.split()

def retira(texto):
    texto2 = texto.replace("=", ": ").replace("+", " ")
    return texto2

if conteudo3[1] == 'resultado=0':
    print('CEP não encontrado ')

else:
    uf = retira(conteudo3[3])
    cidade  = retira(conteudo3[4])
    bairro =  retira(conteudo3[5])
    rua = retira(conteudo3[6]).replace("tipo_logradouro", "") + retira(conteudo3[7]).replace("logradouro", " ")

    print (conteudo3)
    print(uf,cidade,bairro,rua)
