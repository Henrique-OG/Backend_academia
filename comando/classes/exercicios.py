import sqlite3
from rich.console import Console
from rich.table import Table
from comando.classes.treinos import Treinos
from comando.interface import menu_de_exercicios_interface
from comando.utils.validar import validar_escolhas, validar_id_do_treino, validar_id_do_exercicio, validar_num_int

class Exercicio:

    def cadastrar_exercicio(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        nome = input('Digite o nome do exercicio: ').strip()
        grupo_muscular = input('Digite o nome do grupo muscular do exercicio: ').strip()
        description = input('Digite uma descrição para o exercicio: ').strip()

        comando_sql = """INSERT INTO exercicios (nome, grupo_muscular, description) VALUES (?, ?, ?)"""
        cursor.execute(comando_sql, (nome, grupo_muscular, description))

        conexao.commit()
        conexao.close()

        if cursor.rowcount > 0:
            return 'Exercicio cadastrado com sucesso!'
        else:
            return 'Falha ao cadastrar exercicio!'

    def ver_exercicio(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = '''SELECT * FROM exercicios'''
        cursor.execute(comando_sql)
        conteudo = cursor.fetchall()

        t = Table(title='Exercicio')
        t.add_column('id',justify='center')
        t.add_column('exercicio',justify='center')
        t.add_column('grupo_muscular',justify='center')
        t.add_column('description',justify='center', width=30)

        for conteudos in conteudo:
            t.add_row(str(conteudos[0]),str(conteudos[1]),str(conteudos[2]), str(conteudos[3]))

        console = Console()
        console.print(t)

        conexao.close()

    def atribuir_exercicio(self):
        t = Treinos()

        tentativas = 0
        while True:
            t.ver_treinos()
            id_treino = validar_id_do_treino(input('Digite o id do exercicio: '))
            if id_treino != 'ERRO':
                break
            elif id_treino == 'ERRO' and tentativas > 2:
                return 'ERRO ao encontrar treino'
            tentativas += 1

        tentativas = 0
        while True:
            self.ver_exercicio()
            id_exercicio = validar_id_do_exercicio(input('Digite o id do treino: '))
            if id_exercicio != 'ERRO':
                break
            elif id_exercicio != 'ERRO' and tentativas > 2:
                return 'ERRO ao encontrar exercicio'
            tentativas += 1

        series = validar_num_int(input('Digite o numero de series: '))
        repeticoes = validar_num_int(input('Digite o numero de repeticoes: '))

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()
        comando_sql = """INSERT INTO exercicios_treinos (id_treino, id_exercicio, series, repeticoes) VALUES (?, ?, ?, ?)"""
        cursor.execute(comando_sql, (id_treino, id_exercicio, series, repeticoes))

        conexao.commit()
        conexao.close()

        if cursor.rowcount > 0:
            return 'Exercicio cadastrado com sucesso!'
        else:
            return 'Falha ao cadastrar exercicio!'

    def deletar_exercicio(self):

        tentativas = 0
        while True:
            self.ver_exercicio()
            id = validar_id_do_exercicio(input('Digite o id do exercicio: '))
            if id != 'ERRO':
                break
            elif id == 'ERRO' and tentativas > 2:
                return 'ERRO ao encontrar exercicio'
            tentativas += 1

        confirmar = input('Tem certesa que deseja proceguir [S/N]: ').strip().upper()[0]
        while confirmar != 'S' and confirmar != 'N':
            confirmar = input('Responda com S ou N para continuar: ').strip().upper()[0]

        if confirmar == 'S':

            conexao = sqlite3.connect('comando/database/dados.db')
            cursor = conexao.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')
            comando_sql = """DELETE FROM exercicios WHERE id = ?"""
            cursor.execute(comando_sql, (id,))

            conexao.commit()
            conexao.close()

            if cursor.rowcount > 0:
                return 'Exercicio deletado com sucesso!'
            else:
                return 'Falha ao deletar exercicio!'


def menu_de_exercicios():
    exercicio = Exercicio()
    while True:
        menu_de_exercicios_interface()
        escolha_do_usuario = validar_escolhas(input('Digite sua escolha: '), 5)
        if escolha_do_usuario == 1:
            print(exercicio.cadastrar_exercicio())
        elif escolha_do_usuario == 2:
            exercicio.ver_exercicio()
        elif escolha_do_usuario == 3:
            print(exercicio.atribuir_exercicio())
        elif escolha_do_usuario == 4:
            print(exercicio.deletar_exercicio())
        elif escolha_do_usuario == 5:
            break
