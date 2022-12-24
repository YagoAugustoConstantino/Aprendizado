from mysql import connector
import pandas as pd

pd.set_option('display.max_columns',None,)


def ver_tabela(nometabela):
    conexao = connector.connect(host='localhost',
                                user='root',
                                password='Y@g22523464',
                                database='uninter')
    ordenador = conexao.cursor()

    ordem = f'select * from {nometabela}'

    ordenador.execute(ordem)

    coluna = ordenador.column_names

    show = ordenador.fetchall()

    tabela = pd.DataFrame(show, columns=coluna).set_index(coluna[0])

    return print('\n', tabela)


def ver_tabelas_juntas(nometabela1, join1, nometabela2, join2):
    conexao = connector.connect(host='localhost',
                                user='root',
                                password='Y@g22523464',
                                database='uninter')
    ordenador = conexao.cursor()
    ordem = f'select {nometabela1}.*,{nometabela2}.* ' \
            f'from {nometabela1} join {nometabela2} ' \
            f'where {nometabela1}.{join1} = {nometabela2}.{join2}'
    ordenador.execute(ordem)
    colunas = ordenador.column_names
    show = ordenador.fetchall()
    tabela = pd.DataFrame(show, columns=colunas).set_index(f'{join1}')
    return print(tabela)


ver_tabela('CIDADE')
ver_tabelas_juntas('funcionario','cod','cidade','codigo')