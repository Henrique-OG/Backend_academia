from comando.classes.evolucao import Evolucao
from interface import *
from comando.classes.evolucao import *
from comando.classes.alunos import *
from comando.classes.treinos import *
from comando.classes.exercicios import *

def main():

    t = Tabelas()
    t.criar_tabela()
    e = Evolucao()

    while True:
        menu_principal()
        escolha_do_usuario = validar_escolhas(input('Digite sua escolha: '), 7)
        if escolha_do_usuario == 1:
            menu_aluno()
        elif escolha_do_usuario == 2:
            menu_de_treinos()
        elif escolha_do_usuario == 3:
            menu_de_exercicios()
        elif escolha_do_usuario == 4:
            menu_evolucao()
        elif escolha_do_usuario == 7:
            break

    print('Fim do programa')

if __name__ == '__main__':
    main()