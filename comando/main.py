from comando.classes.treinos import Treinos
from comando.database.tabelas import Tabelas
from interface import *
from comando.utils.validar import *
from comando.classes.alunos import *


def main():

    t = Tabelas()
    t.criar_tabela()
    treino = Treinos()

    while True:
        menu_principal()
        escolha_do_usuario = validar_escolhas(input('Digite sua escolha: '), 7)
        if escolha_do_usuario == 1:
            menu_aluno()
        elif escolha_do_usuario == 2:
            pass
        elif escolha_do_usuario == 7:
            break

if __name__ == '__main__':
    main()