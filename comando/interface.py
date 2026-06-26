
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
6 - Relatórios
7 - Encerrar''')
    linha()

def menu_aluno_interface():
    cabecalho('Menu de alunos')
    print('''1 - Cadastrar aluno
2 - Ver alunos cadastrados
3 - Atualizar dados
4 - Excluir aluno
5 - Voltar para menu principal''')
    linha()

def menu_aluno_dados():
    cabecalho('Menu de edição ')
    print('''1 - Editar nome do aluno
2 - Editar idade do aluno
3 - Editar altura do aluno
4 - cancelar

obs: para editar o peso, vá para o menu de evolução''')
    linha()