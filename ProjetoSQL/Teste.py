x = {}
j= 'nome da tabela'.strip( " ' ' " )
for i in range (2):
    nome = input('qual o nome do produto')
    valor =(input('qual o valor do produto'))
    if valor == str:
        valor = str(valor)
    else:
        valor = int(valor)
    x[nome]=valor

print(x.keys())
print(x.values())
k = str(list(x.keys())).strip('[]')
k = k.strip("  ' ' ")
v = str(list(x.values())).strip('[]')

print(x)
