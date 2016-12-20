import sqlite3

class Cadastro:
    def __init__(self):
        self.nome = None
        self.telefone = None

    def cadastrar(nome,telefone):
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO clientes(nome, telefone) VALUES (?,?)',(nome,telefone))
        conn.commit()
        print ("Dados inseridos com sucesso")
        conn.close()
