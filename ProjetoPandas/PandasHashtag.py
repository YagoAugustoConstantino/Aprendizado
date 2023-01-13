import pandas as pd
import plotly.express as px


pd.set_option('display.expand_frame_repr', False)
# pd.set_option('display.max_rows',None)

vendas = pd.read_excel('../ARQUIVOS/Vendas.xlsx')
tabela_vendas = pd.DataFrame(vendas)
# print(tabela_vendas.describe())
# print(tabela_vendas.head())
# print(tabela_vendas.tail().describe())
# print(tabela_vendas)
# print(tabela_vendas['ID Loja'].unique())
lista_lojas = tabela_vendas['ID Loja'].unique()
# print(tabela_vendas[['Produto', 'Quantidade', 'Valor Unitário']])
# print(tabela_vendas.loc[tabela_vendas['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']])
# print(tabela_vendas.loc[752, 'Produto'])
# print(tabela_vendas)
tabela_vendas_dez = pd.read_excel('../ARQUIVOS/Vendas - Dez.xlsx')
tabela_gerentes = pd.read_excel('../ARQUIVOS/Gerentes.xlsx')
tabela_vendas = pd.concat([tabela_vendas, tabela_vendas])
# tabela_vendas = tabela_vendas.merge(tabela_gerentes)
# tabela_vendas['Comissão'] = tabela_vendas['Valor Final']*0.05
# tabela_vendas.loc[:, 'Imposto'] = 0
# tabela_vendas = tabela_vendas.drop('Imposto',axis=1)
# tabela_vendas = tabela_vendas.dropna()
# print(tabela_vendas)
print(tabela_vendas['ID Loja'].value_counts())
# print(tabela_vendas[['Produto','Valor Final']].groupby('Produto').sum())
# print(tabela_vendas[['Produto','Valor Final','Valor Unitário']].groupby('Produto').mean())
tabelageral = tabela_vendas.groupby('ID Loja').sum(numeric_only=True)
tabelageral = tabelageral.sort_values(by="Valor Final", ascending=False)
tabela_vendas = tabela_vendas.dropna(how='all',axis=1)
tabela_vendas = tabela_vendas.dropna(how='all',axis=0)
print(tabela_vendas.info())

print(tabela_vendas['ID Loja'].value_counts())
print(tabelageral)

print(tabela_vendas.describe())

for coluna in tabela_vendas.columns:
    grafico = px.histogram(tabela_vendas, x=coluna, color='Produto', text_auto=True)
    grafico.show()



def nome_loja():
    while True:
        print(str(lista_lojas).strip('[]'), sep='\n,\t')
        loja = input('Coloque o nome da loja para saber seus dados').title()
        while loja not in lista_lojas:
            print('Nome inválido.... tente novamente\n')
            loja = input('Coloque o nome da loja para saber seus dados')
        print(tabela_vendas[tabela_vendas['ID Loja'] == loja])
