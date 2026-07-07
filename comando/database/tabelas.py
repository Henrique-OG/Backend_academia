import sqlite3
from rich.console import Console
from rich.table import Table

class Tabelas():

    def criar_tabela(self):
        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        # Tabela alunos
        comando_sql = """CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                peso REAL NOT NULL,
                altura REAL NOT NULL,
                id_treino INTEGER DEFAULT NULL
                )"""

        cursor.execute(comando_sql)

        # Tabela de treinos
        comando_sql = """CREATE TABLE IF NOT EXISTS treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT NOT NULL
        )"""

        cursor.execute(comando_sql)

        # Tabela de exercicios
        comando_sql = """CREATE TABLE IF NOT EXISTS exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        grupo_muscular TEXT NOT NULL,
        description TEXT NOT NULL
        )"""

        cursor.execute(comando_sql)

        # Tabela de exercicios com treinos
        comando_sql = """CREATE TABLE IF NOT EXISTS exercicios_treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_treino INTEGER NOT NULL,
        id_exercicio INTEGER NOT NULL,
        dia_semana TEXT NOT NULL,
        series INTEGER NOT NULL,
        repeticoes INTEGER NOT NULL,
                
        FOREIGN KEY (id_treino)
        REFERENCES treinos (id)
        ON DELETE CASCADE,
        
        FOREIGN KEY (id_exercicio)
        REFERENCES exercicios (id)
        ON DELETE CASCADE
        )"""

        cursor.execute(comando_sql)

        #tabela de evolução
        comando_sql = """CREATE TABLE IF NOT EXISTS evolucao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aluno INTEGER NOT NULL,
        peso TEXT NOT NULL,
        altura REAL NOT NULL,
        observacao TEXT NOT NULL,
        data TEXT NOT NULL,
        
        FOREIGN KEY (id_aluno)
        REFERENCES alunos (id)
        ON DELETE CASCADE
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
