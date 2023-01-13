import pandas as pd
import plotly.express as px
pd.set_option('display.expand_frame_repr', False)

bd = pd.read_csv(r'../ARQUIVOS/telecom_users.csv')

tabela = pd.DataFrame(bd)

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'],errors='coerce')

tabela = tabela.dropna(how='all', axis=1) # axis 1 == coluna    axis 0 == linha

tabela = tabela.dropna(how='all', axis=0)

cancelamento = tabela['Churn'].value_counts() # mostra uma contagem dos itens com o mesmo nome
cancelamentos = tabela['Churn'].value_counts(normalize=True)# mostra em porcentagem a contagem
# print(tabela.info())
print(tabela)
print(cancelamentos)
print(cancelamento)

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True,color_discrete_sequence=['red','yellow'])
    # etapa 2: exibir o gráfico
    grafico.show(target='blank')

