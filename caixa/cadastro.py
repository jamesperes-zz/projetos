import sqlite3

class Cadastro:
    def __init__(self):
        self.nome = None
        self.telefone = None
        self.tr = None
        self.saldo = None

    def cadastrar(nome,telefone,saldo,tr):
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO clientes(nome, telefone, saldo, tr) VALUES (?,?,?,?)',
                       (nome,telefone,saldo,tr))
        conn.commit()
        print ("Dados inseridos com sucesso")
        conn.close()
