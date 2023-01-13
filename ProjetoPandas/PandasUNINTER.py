import  os


lista_arquivos = os.listdir('../ARQUIVOS')
print(lista_arquivos)
for arquivo in lista_arquivos:
    if 'Vendas' in arquivo:
        print(arquivo)







