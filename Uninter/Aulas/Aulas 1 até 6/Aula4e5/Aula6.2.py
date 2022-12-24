games = []
game1 = {'Nome': 'Mario',
         'Desenvolvedora': 'Nintendo',
         'Ano': 1990}
print(game1)
print(game1['Nome'])
print(game1['Desenvolvedora'])
print(game1['Ano'])
print(game1.values())
print(game1.keys())
print(game1.items())
for i in game1.values():
    print(i)

for i in game1.keys():
    print(i)

for i in game1.items():
    print(i)

for i in game1:
    for items in game1:
        if items == 'Mario:':
            print(items)

game2 = {'Nome': 'Zelda',
         'Desenvolvedora': 'Sega',
         'Ano': 1998}
game3 = {'Nome': 'Sonic',
         'Desenvolvedora': 'Ssega',
         'Ano': 2000}
games.append(game1.copy())
games.append(game2.copy())
games.append(game3.copy())
print(games)

jogo = {}
jogos = []
for i in range(3):
    jogo['Nome'] = input('Qual o nome do jogo ?')
    jogo['Desenvolvedora'] = input('Qual a desenvolvedora?')
    jogo['Ano'] = int(input('Em que ano foi publicado?'))
    jogos.append(jogo.copy())
    jogo.clear()

print(jogos)
print('-' * 20)
for e in jogos:
    for i, j in e.items():
        print('o campo {} tem valor {}'.format(i, j))


