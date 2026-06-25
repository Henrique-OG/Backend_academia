import sqlite3

class Tabelas():

    def criar_tabela(self):
        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = """CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                peso REAL NOT NULL,
                altura REAL NOT NULL
                )"""

        cursor.execute(comando_sql)
        conexao.commit()
        conexao.close()
