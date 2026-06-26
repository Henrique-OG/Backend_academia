import sqlite3
from comando.interface import menu_aluno_interface, menu_aluno_dados
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

    def atualizar_dados(self):
        tentativas = 0
        t = Tabelas()
        while True:
            t.mostrar_id_alunos()
            id = validar_id_do_usuario(input('Digite o id do aluno: '))
            if id == 'ERRO':
                tentativas += 1
            if tentativas > 3:
                return 'ERRO ao acessar dados'
            if tentativas <= 3 and id != 'ERRO':
                break

        while True:
            menu_aluno_dados()
            escolha = validar_escolhas(input('Digite sua escolha: '), 4)
            if escolha == 1:
                escolha = 'nome'
                novo_dado = input('Digite o novo nome do aluno: ').strip().title()
                break
            elif escolha == 2:
                escolha = 'idade'
                novo_dado = validar_num_int(input('Digite a idade do aluno: '))
                break
            elif escolha == 3:
                escolha = 'altura'
                novo_dado = validar_num_float(input('Digite a altura do aluno: '))
                break
            elif escolha == 4:
                return 'Cancelado com sucesso'

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()


        comando_sql = f"""UPDATE alunos SET {escolha} = ? WHERE id = ?"""
        cursor.execute(comando_sql, (novo_dado,id))
        conexao.commit()
        conexao.close()
        return 'Dados alterados com sucesso'

    def excluir_aluno(self):

        t = Tabelas()
        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        tentativas = 0

        while True:
            t.mostrar_id_alunos()
            id = validar_id_do_usuario(input('Digite o id do aluno: '))
            if id == 'ERRO':
                tentativas += 1
            if tentativas > 3:
                return 'ERRO ao acessar dados'
            if tentativas <= 3 and id != 'ERRO':
                break

        comando_sql = "SELECT nome FROM alunos WHERE id = ?"
        cursor.execute(comando_sql, (id,))
        nome = cursor.fetchone()[0]

        print(f'Você tem certeza que deseja excluir a conta de {nome} ? digite S ou N')
        validacao = input('Digite S ou N: ').strip().upper()

        while validacao not in ['N','S']:
            print(f'Você tem certeza que deseja excluir a conta de {nome} ? digite S ou N')
            validacao = input('Digite S ou N: ').strip().upper()


        if validacao == 'N':
            return 'Cancelado com sucesso'
        elif validacao == 'S':
            comando_sql = "DELETE FROM alunos WHERE id = ?"
            cursor.execute(comando_sql, (id,))
            conexao.commit()
            if cursor.rowcount > 0:
                return 'Conta excluida com sucesso'
            else:
                return 'Erro ao excluir conta'
        conexao.close()

def menu_aluno():
    a = Aluno()
    while True:
        menu_aluno_interface()
        escolha = validar_escolhas(input('Digite sua escolha: '), 5)
        if escolha == 1:
            a.cadastrar()
        elif escolha == 2:
            a.ver_alunos()
        elif escolha == 3:
            print(a.atualizar_dados())
        elif escolha == 4:
            print(a.excluir_aluno())
        elif escolha == 5:
            break

