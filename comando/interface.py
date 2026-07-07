
def linha():
    print('-'*50)

def cabecalho(txt):
    linha()
    print(f'{txt: ^50}')
    linha()

def menu_professor_interface():
    cabecalho('Menu professor')
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

def menu_de_treinos_interface():
    cabecalho('Menu de treinos')
    print('''1 - Cadastrar treino
2 - Atribuir treino para aluno
3 - Ver treinos disponiveis
4 - Excluir treino
5 - Voltar''')
    linha()

def menu_de_exercicios_interface():
    cabecalho('Menu de exercicios')
    print('''1 - Cadastrar exercicio
2 - Ver exercicios disponiveis
3 - Vincular exercicio a um treino
4 - Excluir exercicio
5 - Voltar''')
    linha()

def menu_de_evolucao_inteface():
    cabecalho('Menu de evolução')
    print('''1 - Cadastrar evolução
2 - Ver evoluções
3 - voltar''')
    linha()

def menu_principal_interface():
    cabecalho('Menu principal')
    print('''1 - Acessar area professor
2 - Acessar conta do aluno
3 - Sair do programa''')
    linha()

def menu_para_alunos_interface():
    cabecalho('Menu para alunos ')
    print('''1 - Verificar dados
2 - Ver treinos da semana
3 - Marcar presença
4 - ver evolução
5 - baixar relatório
6 - Sair''')
    linha()