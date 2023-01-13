from time import sleep

import pandas as pd
from mysql import connector

pd.set_option('display.expand_frame_repr', False)

# Conexão com o MySql
conexao = connector.connect(host='localhost',
                            user='root',
                            password='Y@g22523464',
                            database='uninter')


# CRUD em Python e Sql, usando pandas para visualização de tabelas


# Criando a função para visualizar uma tabela em python
def ver_tabela():
    ordenador = conexao.cursor()
    nometabela = str(input('Qual o nome da tabela que vc deseja visualizar ?'))

    ordem = f'select * from {nometabela};'

    ordenador.execute(ordem)

    coluna = ordenador.column_names

    show = ordenador.fetchall()

    tabela = pd.DataFrame(show, columns=coluna).set_index(coluna[0])

    return print('\n', tabela)


# Criando a função para visualizar duas tabelas juntas em python
def ver_tabelas_juntas():
    nometabela1 = str(input('Qual o nome da  primeira tabela que vc deseja juntar ?'))
    join1 = str(input('Qual a coluna da primeira tabela  que vc deseja que seja a base da junção ?'))
    nometabela2 = str(input('Qual o nome da  segunda tabela que vc deseja juntar ?'))
    join2 = str(input('Qual a coluna da segunda tabela  que vc deseja que seja a base da junção ?'))
    ordenador = conexao.cursor()
    ordem = f'select {nometabela1}.*,{nometabela2}.* ' \
            f'from {nometabela1} join {nometabela2} ' \
            f'where {nometabela1}.{join1} = {nometabela2}.{join2};'
    ordenador.execute(ordem)
    colunas = ordenador.column_names
    show = ordenador.fetchall()
    tabela = pd.DataFrame(show, columns=colunas).set_index(f'{join1}')
    return tabela


# Criando a função para ver as colunas da tabela
def nome_das_colunas():
    nometabela = str(input('Qual o nome da tabela que vc deseja ver as colunas  ?'))
    ordenador = conexao.cursor()
    ordem = f'select * from {nometabela};'
    ordenador.execute(ordem)
    colunas = ordenador.column_names
    colunas2 = str(colunas).strip('()')
    colunas3 = colunas2.replace("'", "")
    print(colunas3)
    return colunas


# Criando a função para visualizar como os dados estão organizados na tabela
def describe():
    nometabela = str(input('Qual o nome da tabela que vc deseja visualizar ?'))
    ordenador = conexao.cursor()
    ordem = f'describe {nometabela};'
    ordenador.execute(ordem)
    coluna = ordenador.column_names

    show = ordenador.fetchall()

    tabela = pd.DataFrame(show, columns=coluna).set_index(coluna[0])
    print(tabela)
    return tabela


# Criando a função para inserir dados em uma tabela
def inserir():
    nometabela = str(input('Qual o nome da tabela que vc deseja inserir dados  ?'))
    ordenador = conexao.cursor()
    nome_colunas = {}
    print('Colunas da sua tabela :')
    colunas = nome_das_colunas()
    lista_colunas = []
    for item in colunas:
        lista_colunas.append(item)
    del lista_colunas[0]
    for coluna in lista_colunas:
        value = input(f'Qual valor vc deseja colocar na coluna {coluna}? :')
        for v in value:
            if v in '1234567890':
                value = int(value)
        nome_colunas[coluna] = value
    lista_colunas = str(list(nome_colunas.keys())).strip(" []")
    lista_values = str(list(nome_colunas.values())).strip('[]')
    lista_colunas = lista_colunas.replace("'", "")
    nometabela = nometabela.strip("  ' ' ")
    ordem1 = f'insert into {nometabela} ({lista_colunas}) values ({lista_values}); '
    ordenador.execute(ordem1)

    return conexao.commit()


# Criando a função para deletar uma linha na tabela
def deletar_linha():
    nometabela = str(input('Qual o nome da tabela que você deseja deletar um item ?'))
    cod = int(input('Qual o codigo do item que vc deseja deletar ?'))
    lista_colunas = []
    colunas = nome_das_colunas()
    for coluna in colunas:
        lista_colunas.append(coluna)

    ordenador = conexao.cursor()
    ordem = f'delete from {nometabela} where {lista_colunas[0]} = {cod};'
    ordenador.execute(ordem)
    print('Linha excluida com sucesso....\n')
    return conexao.commit()


# Criando a função para deleter uma coluna inteira na tabela
def deletar_coluna():
    nometabela = str(input('Qual o nome da tabela que vc deseja visualizar ?'))
    coluna = str(input('Qual a coluna que vc deseja excluir ?'))
    ordenador = conexao.cursor()
    ordem = f'alter table {nometabela} drop column {coluna};'
    ordenador.execute(ordem)
    print('Coluna deletada com sucesso...')
    return conexao.commit()


# Criando a função de  deletar uma tabela
def deletar_tabela():
    nometabela = str(input('Qual o nome da tabela que vc deseja visualizar ?'))
    ordenador = conexao.cursor()
    ordem = f'drop table {nometabela};'
    ordenador.execute(ordem)
    print('Coluna deletada com sucesso...')
    return conexao.commit()


# Função para atualizar uma linha
def atualizar_dado():
    nometabela = str(input('Qual a tabela que receberá a atualização ?'))
    colunamudada = str(input('Qual a coluna do item será mudada ?'))
    mudanca = str(input('O Novo Valor que será inserido ?'))
    cod = str(input('Qual o codigo do Valor antigo ?'))
    for m in mudanca:
        if m in '1234567890':
            mudanca = int(mudanca)
        else:
            mudanca = str(mudanca)
    lista_colunas = []
    colunas = nome_das_colunas()
    for coluna in colunas:
        lista_colunas.append(coluna)
    ordenador = conexao.cursor()
    ordem = f'update {nometabela} set {colunamudada} = {mudanca} where {lista_colunas[0]} = {cod};'
    ordenador.execute(ordem)
    print(f'Coluna {colunamudada} foi atualizada...Novo valor = {mudanca} ')
    return conexao.commit()


# Função para mostrar todas as tabelas
def mostrar_tabelas():
    ordenador = conexao.cursor()
    ordem = f'show tables'
    ordenador.execute(ordem)
    coluna = ordenador.column_names
    show = ordenador.fetchall()
    tabela = pd.DataFrame(show, columns=coluna, index=coluna[0])
    return print(tabela)


# Função para criar uma tabela
def criar_tabela():
    nometabela = str(input('insira o nome da sua tabela'))
    lista_coluna = []
    lista_tipo = []
    tabela = {}
    while True:
        print('Deseja Insirar uma Coluna ? [S/N]:')
        op = input('').strip().upper()[0]
        if op in 'sS':
            coluna = str(input('Qual o nome da coluna ?'))
            lista_coluna.append(coluna)
            continue
        elif op in 'nN':
            break
        else:
            print('Opção inválida ..tente novamente')
            continue

    for coluna in lista_coluna:
        while True:
            tipo = str(input(f'Qual o tipo da sua coluna {coluna} ?[TEXTO][NUMERO]')).strip().upper()[0]
            if tipo in 'tT':
                lista_tipo.append('varchar(100) not null')
                break
            elif tipo in 'nN':
                lista_tipo.append('int not null')
                break
            else:
                print('valores inválidos.. tente novamente usando TEXTO ou NUMERO')
    for c, t in zip(lista_coluna, lista_tipo):
        tabela[c] = t
    tabela = str(tabela).strip('{}')
    tabela = tabela.replace(":", "")
    tabela = tabela.replace("'", "")

    ordenador = conexao.connect()
    ordem = f'create database {nometabela} ({tabela},primary key ({lista_coluna[0]}))'
    ordenador.execute(ordem)
    print('Tabela criada com sucesso')
    return conexao.commit()


# Começo do MENU PRINCIPAL// Criação dos Menus internos
def menu_ver_tabelas():
    while True:
        print('1 - Ver o nome de todas as tabelas')
        print('2 - Ver a descrição de uma tabela especifica')
        print('3 - Ver uma tabela especifica')
        print('4 - Ver Duas tabelas ligadas entre si ')
        print('5 - Ver o nome das colunas de uma tabela determinada')
        print('6 - Retornar ao Menu Principal', end=' ')
        opmenuprincipal = int(input(':'))
        if opmenuprincipal == 1:
            mostrar_tabelas()
            print('\n')
            sleep(1)
            continue
        elif opmenuprincipal == 2:
            describe()
            print('\n')
            sleep(1)
            continue
        elif opmenuprincipal == 3:
            ver_tabela()
            print('\n')
            sleep(1)
            continue
        elif opmenuprincipal == 4:
            ver_tabelas_juntas()
            print('\n')
            sleep(1)
            continue
        elif opmenuprincipal == 5:
            nome_das_colunas()
            print('\n')
            sleep(1)
            continue
        elif opmenuprincipal == 6:
            break


def menu_deletar():
    while True:
        print('1 - Deletar Tabela')
        print('2 - Deletar Coluna')
        print('3 - Deletar linha')
        print('4 - Retornar ao Menu Principal', end='')
        opmenudeletar = int(input(':'))
        if opmenudeletar == 1:
            sleep(0.5)
            deletar_tabela()
            print('\n')
            sleep(0.5)
            continue
        elif opmenudeletar == 2:
            sleep(0.5)
            deletar_coluna()
            print('\n')
            sleep(0.5)
            continue
        elif opmenudeletar == 3:
            sleep(0.5)
            deletar_linha()
            print('\n')
            sleep(0.5)
            continue
        elif opmenudeletar == 4:
            print('Retornando ao Menu Principal....')
            sleep(0.5)
            break


print('Bem Vindo ao Banco de Dados DYB ')
while True:
    print('1 - Criar Uma Tabela')
    print('2 - Acessar Uma Tabela')
    print('3- Atualizar Um Item')
    print('4 - Deletar ')
    print('5 - Sair do Programa ', end='')
    opMenuVerTabela = int(input(':'))
    if opMenuVerTabela == 1:
        sleep(0.5)
        criar_tabela()
        sleep(0.5)
        continue
    elif opMenuVerTabela == 2:
        sleep(0.5)
        menu_ver_tabelas()
        sleep(0.5)
        continue
    elif opMenuVerTabela == 3:
        sleep(0.5)
        atualizar_dado()
        print('\n')
        sleep(0.5)
        continue
    elif opMenuVerTabela == 4:
        sleep(0.5)
        menu_deletar()
        sleep(0.5)
        continue
    elif opMenuVerTabela == 5:
        break
    else:
        print('Opção inválida...Tente um Número entre 1 e 5 ')
        sleep(0.5)
        continue
