import sqlite3
from rich.console import Console
from rich.table import Table
from comando.classes.alunos import Aluno
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
        dados = cursor.execute(comando_sql)

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