import sqlite3
from rich.console import Console
from rich.table import Table

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

    def mostrar_id_alunos(self):
        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        cursor.execute("""SELECT id,nome FROM alunos""")
        dados = cursor.fetchall()

        t = Table(title='alunos')
        t.add_column('id', justify='center')
        t.add_column('nome', justify='center')

        for dado in dados:
            t.add_row(str(dado[0]), str(dado[1]))

        console = Console()
        console.print(t)

        conexao.close()
