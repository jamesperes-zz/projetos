import sqlite3


#conecta ao banco de dados
conn = sqlite3.connect('clientes.db')

#define um cursor //é um interador que permite navegar e manipular o registros do bd
cursor = conn.cursor()


#criando a tabela (schema)
cursor.execute("""
CREATE TABLE clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        saldo VARCHAR,
        tr TEXT
);
""")

print ("Tabela criada com sucesso. ")


conn.close()
