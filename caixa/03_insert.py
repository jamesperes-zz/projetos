import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


#inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome,telefone)
VALUES ('joao da silva','777-1234')
""")

cursor.execute("""
INSERT INTO clientes (nome,telefone)
VALUES ('maria da silva','444-1234')
""")


#gravando no bd
conn.commit()

print('Dados inseridos com sucesso')

conn.close()
