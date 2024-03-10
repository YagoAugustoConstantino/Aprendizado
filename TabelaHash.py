caderno = {}
caderno['Maçã'] = 0.67
caderno['Leite'] = 1.49
caderno['Abacate']= 1.49
for i in caderno:
    print(f'O item {i} tem o valor de {caderno[i]}')


print('\n')
lista_telefonica = {}
lista_telefonica ['Jenny'] = 8675309
lista_telefonica ['Emergencia'] = 190
for i in lista_telefonica:
    print(f'o numero de {i} é {lista_telefonica[i]}')

def verifica(nome):
    if caderno.get(nome):
        print('Existe no caderno')
    else:
        print('Esse item ainda nao foi cadastrado .... Efetue o cadastro')
        name = input(str('Qual o nome do item ?'))
        valor = input('Qual o valor do item ?')
        caderno[name] = float(valor)
        return caderno
verifica('Banana')
print(caderno)
# Os dicionarios e uso de mapas hash ou tabelas (todas as mesma coisa) é
# comum em caches de sites e para guardar URl,assim evitando de fazer uma
# busca no servidor apenas para acessar uma pagina.