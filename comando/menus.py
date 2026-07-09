from comando.classes.area_aluno import Area_aluno
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

def area_aluno_menu(id):
    a = Area_aluno(id)

    while True:
        menu_para_alunos_interface()
        escolha = validar_escolhas(input('Digite sua escolha: '), 7)
        if escolha == 1:
            a.verificar_dados()
        elif escolha == 2:
            a.ver_treino_semana()
        elif escolha == 3:
            print(a.marcar_presenca())
        elif escolha == 4:
            a.ver_evolucao()
        elif escolha == 6:
            a.ver_presencas()
        elif escolha == 7:
            break