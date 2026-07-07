from comando.menus import *
from time import sleep

def main():

    t = Tabelas()
    t.criar_tabela()

    while True:
        menu_principal_interface()
        sleep(1)
        escolha = validar_escolhas(input('Digite sua escolha: '), 3)
        if escolha == 1:
            sleep(1)
            menu_professor()
        elif escolha == 2:
            sleep(1)
            tentativas = 0
            while True:
                id = validar_id_do_usuario(input('Digite o id do aluno: '))
                if id == 'ERRO' and tentativas > 3 or id != 'ERRO':
                    break
                tentativas += 1
            if id == 'ERRO':
                print('Erro ao acessar dados..')
            else:
                area_aluno_menu(id)
        elif escolha == 3:
            break

    print('Fim do programa')

if __name__ == '__main__':
    main()