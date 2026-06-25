import sqlite3
from comando.utils.validar import *
from rich.table import Table
from rich.console import Console

class Aluno():

    def cadastrar(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = """INSERT INTO alunos (nome, idade, peso, altura) VALUES (?,?,?,?)"""

        nome = input('Digite o nome do aluno: ').strip().title()
        idade = validar_num_int(input('Digite a idade do aluno: '))
        peso = validar_num_float(input('Digite o peso do aluno: '))
        altura = validar_num_float(input('Digite a altura do aluno: '))

        cursor.execute(comando_sql, (nome, idade, peso, altura))
        conexao.commit()
        conexao.close()

    def ver_alunos(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = """SELECT * FROM alunos"""
        cursor.execute(comando_sql)

        dados = cursor.fetchall()

        tabela = Table(title="Alunos", title_justify='center')
        tabela.add_column('id', justify='center')
        tabela.add_column('nome', justify='center')
        tabela.add_column('idade', justify='center')
        tabela.add_column('peso', justify='center')
        tabela.add_column('altura', justify='center')

        for aluno in dados:
            id, nome, idade, peso, altura = aluno
            tabela.add_row(str(id), str(nome), str(idade), str(peso), str(altura))

        console = Console()
        console.print(tabela)

        conexao.close()
