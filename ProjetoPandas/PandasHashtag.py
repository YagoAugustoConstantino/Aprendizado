import pandas as pd
pd.set_option('display.expand_frame_repr',False)
#pd.set_option('display.max_rows',None)
vendas = pd.read_excel('../ARQUIVOS/Vendas.xlsx')
tabela_vendas = pd.DataFrame(vendas)
#print(tabela_vendas.describe())
#print(tabela_vendas.head())
#print(tabela_vendas.tail().describe())
#print(tabela_vendas)
#print(tabela_vendas['ID Loja'].unique())
lista_lojas = tabela_vendas['ID Loja'].unique()

def nome_loja():
    print(str(lista_lojas).strip('[]'), end=' \n ')
    loja = input('coloque o nome da loja para saber seus dados').title()
    print(tabela_vendas[tabela_vendas['ID Loja'] == loja])
nome_loja()