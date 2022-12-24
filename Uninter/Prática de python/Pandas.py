from pandas import *
set_option('display.expand_frame_repr',False)
tabela_pokemon = read_csv('../../ARQUIVOS/pokemon.txt')
x = DataFrame(tabela_pokemon)
tabela_vendas = read_excel('../../ARQUIVOS/Vendas.xlsx')
lojaiguatemi = tabela_vendas[tabela_vendas['ID Loja'] == 'Iguatemi Esplanada']
produtos = tabela_vendas[['Produto', 'Valor Final']]
tabela_vendas_dez = read_excel('../../ARQUIVOS/Vendas - Dez.xlsx')
print(tabela_vendas)
tabela_vendas = concat([tabela_vendas, tabela_vendas_dez])
print(tabela_vendas)
print(tabela_pokemon)





