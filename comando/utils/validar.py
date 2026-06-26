import sqlite3
from rich.console import Console
from rich.table import Table

from comando.database.tabelas import Tabelas


def validar_num_int(num):
    while not num.isnumeric():
        num = input("Digite um número inteiro: ")
    return int(num)

def validar_escolhas(escolha, maximo):
    escolha = validar_num_int(escolha)
    while escolha > maximo:
        escolha = validar_num_int(input('Digite uma escolha valida: '))
    return escolha

def validar_num_float(num):
    while not num.replace('.', '').isnumeric():
        num = input('Digite um valor valido: ')
    return float(num)

def validar_id_do_usuario(id_usuario):

    id_usuario = validar_num_int(id_usuario)

    conexao = sqlite3.connect('comando/database/dados.db')
    cursor = conexao.cursor()

    comando_sql = """SELECT * FROM alunos WHERE id = ?"""
    cursor.execute(comando_sql, (id_usuario,))

    dados = cursor.fetchone()

    if dados == None:
        return 'ERRO'
    else:
        return dados[0]



