mochila = ['casa' , 'escola' , 'trabalho' , 'hospital']
print(mochila[0])
print(mochila[1])
print(mochila[2])
print(mochila[3])
print(mochila[3][0])
print(mochila[3][1])
print(mochila[3][2])
print(mochila[3][3])
print(mochila[3][0:])
print(mochila[3][3:])
for item in mochila:
    for letra in item:
        print(letra, end='')

item = []
mercado = []
for i in range(3):
    item.append(input('Qual o nome do produto?'))
    item.append(int(input('Quantos produtos você deseja ?')))
    item.append(float(input('Qual o valor do produto?')))
    mercado.append(item[:])
    item.clear()
print(mercado)

game={'nome' : 'Mario',
      'desenvolvedora' : 'Nintendo',
       'Ano':'1990'}
print(game)
print(game['nome'])
print(game['desenvolvedora'])
print(game['Ano'])

