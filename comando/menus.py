from interface import *
from comando.classes.evolucao import *
from comando.classes.alunos import *
from comando.classes.treinos import *
from comando.classes.exercicios import *

def menu_professor():
    while True:
        menu_professor_interface()
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

