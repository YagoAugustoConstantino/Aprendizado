def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        print('Opção Inválida...Tente Novamente:')
        x = int(input(pergunta))
    return x


listaprodutos = []

code: int = 1


# ---cadastrar produto---
def Cadastrar_produto(code):
    print('Bem vindo ao Cadastro de Produtos')
    print(f'o Código do produto a ser cadastrado é:{code}')
    Nome = input('Digite  o nome do produto:\n')
    Valor = int(input('Digite  o valor do produto:\n'))
    Fabricante = input('Digite o fabricante do produto\n')
    dicionario_produtos = {'Nome': Nome,
                           'Fabricante': Fabricante,
                           'Valor': Valor,
                           'Código': code}
    listaprodutos.append(dicionario_produtos.copy())
    code += 1


# ----- Fim do Cadastro---


def Consulta_produto():  # ---Começao de consulta por produto---
    print('Bem vindo a Consulta de Produtos')
    while True:
        try:
            print('1-Consultar todos os produtos')
            print('2-Consultar por Código')
            print('3-Consultar por Fabricante')
            print('4-Retornar')
            opcao2 = int(input('Escolha uma Tarefa a ser executada\n'))  # Consulta todos os produtos cadastrados
            if opcao2 == 1:
                print('Bem vindo a Consultar todos os produtos')
                for produto in listaprodutos:  # seleciona cada dicionário de minha lista
                    for key, value in produto.items():  # seleciona cada conjunto chave/valor do dicionário(nome/leite)
                        print('{}:{}\n'.format(key, value))  # imprime cada conjunto

            elif opcao2 == 2:
                print('Bem vindo a Consultar por Código')
                entrada = int(input('Qual o Código do produto?:\n'))
                for produto in listaprodutos:
                    if produto['Código'] == entrada:
                        for key, value in produto.items():
                            print('{}:{}\n'.format(key, value))
            elif opcao2 == 3:
                print('Bem vindo a Consultar por Fabricante')
                entrada = input('Qual o nome do Fabricante?:')
                for produto in listaprodutos:
                    if produto['Fabricante'] == entrada:
                        for key, value in produto.items():
                            print('{}:{}\n'.format(key, value))

            elif opcao2 == 4:
                print('Retornando ao Menu Principal')
                return
            else:
                print('Opção inválida...Tente novamente')
                continue
        except ValueError:
            print('É necessário usar um código que seja um número inteiro e positivo entre 1 e 4 ')


# ____Fim da consulta____

# ------Começo da Remoção---
def Remover_produto():
    print('Bem vindo a Remoção de produtos')
    entrada = int(input('Qual o Código do produto a ser removido?:'))
    for produto in listaprodutos:
        if produto['Código'] == entrada:
            listaprodutos.remove(produto)
            # ------------Fim da Remoção-----------

# lista = []
# dado = []
# for i in range(0, 4):
# dado.append(str(input('Insira o nome da pessoa')))
# dado.append(int(input('insira o peso da pessoa')))
# lista.append(dado[:])
# dado.clear()

# for g, p in lista:
# print(f' a pessoa {g} pesa {p} KG ')

# if len(lista) == 0:
# maior = menor = variavel
# else:
# if variavel > maior:
#  maior = variavel
# elif variavel < menor:
#  menor = variavel
