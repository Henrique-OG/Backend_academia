
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

def menu_aluno():
    cabecalho('Menu de alunos')
    print('''1 - Cadastrar aluno
2 - Ver alunos cadastrados
3 - Atualizar dados
4 - Excluir aluno
5 - Voltar para menu principal''')