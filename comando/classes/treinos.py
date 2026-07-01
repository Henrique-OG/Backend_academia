import sqlite3
from rich.console import Console
from rich.table import Table
from comando.classes.alunos import Aluno
from comando.interface import cabecalho, menu_de_treinos_interface
from comando.utils.validar import validar_id_do_usuario, validar_escolhas, validar_id_do_treino


class Treinos():

    def cadastrar_treinos(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        nome = input('Digite o nome do treino: ').strip()
        descricao = input('De uma descrição para o treino: ').strip()

        comando_sql = '''INSERT INTO treinos (nome, description) VALUES (?, ?)'''
        cursor.execute(comando_sql, (nome, descricao))
        conexao.commit()

        if cursor.rowcount > 0:
            print('Treino cadastrado com sucesso!')
        else:
            print('ERRO ao cadastrar treino')

        conexao.close()

    def ver_treinos(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = '''SELECT * FROM treinos'''
        cursor.execute(comando_sql)

        dados = cursor.fetchall()

        t = Table(title='Treinos')
        t.add_column('id', justify='center')
        t.add_column('nome', justify='center')
        t.add_column('descrição', justify='center', width=46)

        for itens in dados:
            t.add_row(str(itens[0]), str(itens[1]), str(itens[2]))
        console = Console()
        console.print(t)
        print(f'total: {len(dados)}')
        conexao.close()

    def atribuir_treino(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        tentativas = 0
        comando_sql = '''SELECT id, nome FROM alunos'''
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        if dados == []:
            return 'erro ao acessar dados, sem alunos cadastrados'


        while True:
            for dado in dados:
                print(f'{dado[0]} - {dado[1]}')
            id = validar_id_do_usuario(input('Digite o id do aluno: '))
            if id == 'ERRO' and tentativas > 3:
                return 'ERRO ao encontrar o id do aluno'
            tentativas += 1
            if id != 'ERRO':
                break


        while True:
            Treinos.ver_treinos(self)
            id_treino = validar_id_do_treino(input('Digite o id do treino: '))
            if id_treino == 'ERRO' and tentativas > 3:
                return 'ERRO ao acessar dados'
            tentativas += 1
            if id_treino != 'ERRO':
                break

        comando_sql = '''UPDATE alunos SET id_treino = ? WHERE id = ?'''
        cursor.execute(comando_sql, (id_treino, id))
        conexao.commit()
        conexao.close()

        if cursor.rowcount > 0:
            return 'Treino atualizado com sucesso!'
        else:
            return 'erro ao alterar dados'

    def deletar_treino(self):

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        tentativas = 0

        while True:
            Treinos.ver_treinos(self)
            continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
            while continuar not in 'SN':
                continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
            if continuar == 'N':
                return 'cancelado com sucesso!'
            id_treino = validar_id_do_treino(input('Digite o id do treino: '))
            if id_treino == 'ERRO' and tentativas > 3:
                return 'ERRO ao acessar dados'
            tentativas += 1
            if id_treino != 'ERRO':
                break

        resposta = input('Certeza que deseja deletar o treino [S/N]: ').upper().strip()[0]
        while resposta != 'S' and resposta != 'N':
            resposta = input('Digite S para sim e N para não: ').upper().strip()[0]

        if resposta == 'N':
            return 'cancelado com sucesso!'
        else:
            comando_sql = """DELETE FROM treinos WHERE id = ?"""
            cursor.execute(comando_sql, (id_treino,))
            comando_sql = """UPDATE alunos SET id_treino = ? WHERE id_treino = ?"""
            cursor.execute(comando_sql, ( None , id_treino))
            conexao.commit()
            conexao.close()
            if cursor.rowcount > 0:
                return 'Treino excluido com sucesso!'
            else:
                return 'erro ao alterar dados'

def menu_de_treinos():
    t = Treinos()
    while True:
        menu_de_treinos_interface()
        resposta_do_usuario = validar_escolhas(input('Digite sua escolha: '), 5)
        if resposta_do_usuario == 1:
            t.cadastrar_treinos()
        elif resposta_do_usuario == 2:
            print(t.atribuir_treino())
        elif resposta_do_usuario == 3:
            t.ver_treinos()
        elif resposta_do_usuario == 4:
            print(t.deletar_treino())
        elif resposta_do_usuario == 5:
            break
