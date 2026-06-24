
def linha():
    print('-'*50)

def cabecalho(txt):
    linha()
    print(f'{txt: ^50}')
    linha()

def menu_principal():
    cabecalho('Menu principal')
    print('''1 - Alunos
2 - Treinos
3 - Exercicios
4 - evolução
5 - Frequência
6 - Relatórios''')
    linha()