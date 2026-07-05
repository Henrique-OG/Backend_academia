from comando.database.tabelas import Tabelas
from comando.interface import menu_de_evolucao_inteface
from comando.utils.validar import validar_id_do_usuario, validar_num_float, validar_escolhas
from datetime import datetime
import sqlite3

class Evolucao():

    def registrar_evolucao(self):
        t = Tabelas()
        tentativas = 0
        while True:
            t.mostrar_id_alunos()
            id_aluno = validar_id_do_usuario(input('Digite o id do aluno: '))
            if id_aluno != 'ERRO':
                break
            elif id_aluno == 'ERRO' and tentativas > 3:
                return 'ERRO ao encontrar usuario'
            tentativas += 1

        peso = validar_num_float(input('Digite o peso do aluno: '))
        altura = validar_num_float(input('Digite o altura do aluno: '))
        observacao = input('Digite uma observação para o aluno: ')
        data = datetime.today().strftime('%d/%m/%Y')

        conexao = sqlite3.connect('comando/database/dados.db')
        cursor = conexao.cursor()

        comando_sql = """INSERT INTO evolucao (id_aluno, peso, altura, observacao, data) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(comando_sql, (id_aluno, peso, altura, observacao, data))

        comando_sql = """UPDATE alunos SET peso = ? WHERE id = ? """
        cursor.execute(comando_sql, (peso, id_aluno))

        comando_sql = """UPDATE alunos SET altura = ? WHERE id = ? """
        cursor.execute(comando_sql, (altura, id_aluno))
        conexao.commit()
        conexao.close()

        if cursor.rowcount > 0:
            return 'Evolução dadastrada com sucesso'
        else:
            return 'Erro ao cadastrar'

def menu_evolucao():
    e = Evolucao()
    while True:
        menu_de_evolucao_inteface()
        resposta_do_usuario = validar_escolhas(input('Digite sua escolha: '), 3)
        if resposta_do_usuario == 1:
            e.registrar_evolucao()
        elif resposta_do_usuario == 3:
            break


