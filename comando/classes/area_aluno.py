import sqlite3
from rich.console import Console
from rich.table import Table

class Area_aluno():
    def __init__(self, id):
        self.id = id

    def verificar_dados(self):
        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = """SELECT * FROM alunos WHERE id = ?"""
        cursor.execute(comando_sql, (self.id,))
        dados = cursor.fetchall()

        t = Table(title="dados")
        t.add_column('id', justify='center')
        t.add_column('nome', justify='center')
        t.add_column('idade', justify='center')
        t.add_column('peso', justify='center')
        t.add_column('altura', justify='center')
        t.add_column('id_treino', justify='center')

        for dado in dados:
            t.add_row(str(dado[0]), str(dado[1]), str(dado[2]), str(dado[3]), str(dado[4]), str(dado[5]))

        console = Console()
        console.print(t)

        conexao.close()