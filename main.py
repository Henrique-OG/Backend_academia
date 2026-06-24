from menu import *
from utils.validar import *


def main():
    while True:
        menu_principal()
        escolha_do_usuario = validar_escolhas(input('Digite sua escolha: '), 6)
        if escolha_do_usuario == 6:
            break

if __name__ == '__main__':
    main()