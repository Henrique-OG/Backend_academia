
def validar_num_int(num):
    while not num.isnumeric():
        num = input("Digite um número inteiro: ")
    return int(num)

def validar_escolhas(escolha, maximo):
    escolha = validar_num_int(escolha)
    while escolha > maximo:
        escolha = validar_num_int(input('Digite uma escolha valida: '))
    return escolha