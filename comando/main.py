from comando.classes.treinos import Treinos
from comando.database.tabelas import Tabelas
from interface import *
from comando.utils.validar import *
from comando.classes.alunos import *
from comando.classes.treinos import *

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
            menu_de_treinos()
        elif escolha_do_usuario == 7:
            break

    print('Fim do programa')

if __name__ == '__main__':
    main()