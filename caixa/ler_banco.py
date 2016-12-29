
class Ler(object):
    def localizar_cliente(self, id):
        r = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE id = ?', (id,))
        return r.fetchone()

    def imprimir_cliente(self, id):
        if self.localizar_cliente(id) == None:
            print('Não existe cliente com o id informado.')
        else:
            print(self.localizar_cliente(id))
