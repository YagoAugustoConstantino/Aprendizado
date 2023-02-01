# pessoas = {'nome': 'Yago', 'name': 'Joao', 'Sexo': 'M', 'Idade': 21}
# print(pessoas)
# print(pessoas.keys())
# print(pessoas.get('nome'))
# print(pessoas.values())
# print(pessoas['name'])
# or key, value in pessoas.items():
#   print(f'{key, value}'.replace("'", "").strip('()'))
# dico = {}
# cont = 0
# lista1 = ['Yago', 'Joao', 'Ana', 'Etiene']
# lista2 = [20, 20, 24, 32]
# for item in lista1:
#   dico[item] = lista2[cont]
#   cont += 1

# print(dico)
# brasil = []
# estado = {}

# for i in range(0,3):
#   estado['UF'] = str(input('ESTADO'))
#   estado['Sigla'] = str(input('Sigla do ESTADO'))
#   brasil.append(estado.copy())

# print(brasil)

# aluno = {}
# alunos = []
# for i in range(0, 3):
#   aluno['Nome'] = str(input('Qual o nome do Aluno ?'))
#  aluno['Média'] = float(input('Qual a nota do Aluno ?'))
# if aluno['Média'] >= 7:
#    aluno['Situação'] = 'Aprovado'
# else:
#   aluno['Situação'] = 'Reprovado'
# alunos.append(aluno.copy())

# print(alunos)
# for aluno in alunos:
#   for k, v in aluno.items():
#      print(f' {k} é igual {v}')
# print('\n')
# from random import randint
# from time import sleep
# from operator import itemgetter

# jogo = {
#   'jogador1': randint(1, 6),
#  'jogador2': randint(1, 6),
# 'jogador3': randint(1, 6),
# 'jogador4': randint(1, 6)
# }
# ranking = {}

# print(sorted(jogo.values()))
# for k, v in jogo.items():
#   print(k, v)
#  sleep(1)

# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# for k, v in enumerate(ranking):
#   print(f' {k + 1} lugar :{v[0]} tirou {v[1]} no dado ')
# from datetime import datetime
# dados = {}
# dados['nome'] = str(input('Qual o seu nome ?'))
# anodenascimento = int(input('Em que ano vc nasceu ?'))
# dados['idade'] = datetime.now().year - anodenascimento
# dados['CTPS'] = int(input('Qual o número da sua carteira ?[0 caso não tenha]'))
# if dados['CTPS'] != 0:
#   dados['contrataçao'] = int(input('Qual o Ano de contrataçaõ?'))
#  dados['Sálario'] = float(input('Qual o seu salário'))
# dados['Aposentadoria'] = (dados['contrataçao'] + 35) - (datetime.now().year)


# for k, v in dados.items():
#   if k =='Aposentadoria':
#      print(f'-{k} será com {v} anos  ')
# else:
#    print(f'-{k} tem o valor de {v}')

jogador ={}
jogador['nome'] = str(input('Qual o nome do jogador ?'))
jogador['partidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou ?'))
gols = []
cont = 1
totgol = 0
while cont <= jogador['partidas']:
    g = int(input(f'Quantos gols o {jogador["nome"]} fez na partida {cont} '))
    cont += 1
    gols.append(g)
jogador['gols'] = gols

for i in gols:
    totgol += i

jogador['totaldegols'] = totgol


print(jogador)
for k , v in jogador.items():
    print(f' o campo {k} tem valor {v}')

print(f'O Jogador {jogador["nome"]} jogou um total de {jogador["partidas"]} ')
for l in range(0,jogador['partidas']):
    print(f' => Na partida {l+1},fez {gols[l]} gols .')

print(f'foi um total de {totgol} gols')
