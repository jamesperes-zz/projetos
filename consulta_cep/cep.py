from urllib import request
from urllib.parse import parse_qs


class Endereco():
    def __init__(self, cep):
        self.cep = None
        self.uf = None
        self.cidade = None
        self.bairro = None
        self.rua = None
        self.tipo = None

        self.url_api  = "http://cep.republicavirtual.com.br/web_cep.php?cep={}&formato=query_string"

        self.consulta_por_cep(cep)

    def consulta_por_cep(self, cep):
        print("consultando pelo CEP: " + cep + ".")

        response = request.urlopen(
            self.url_api.format(cep))

        dict_formatado = self.formata_resposta_api(response)
        self.cep = cep
        self.uf = dict_formatado['uf']
        self.cidade = dict_formatado['cidade']
        self.bairro = dict_formatado['bairro']
        self.rua = dict_formatado['logradouro']
        self.tipo = dict_formatado['tipo_logradouro']

    def formata_resposta_api(self,response):
        pagina_str = response.read().decode()
        retorno_dict = parse_qs(pagina_str)
        return { k:v[0] for k,v in retorno_dict.items() }





#minha_rua = Endereco(cep='21310310')
#print(minha_rua.rua)
