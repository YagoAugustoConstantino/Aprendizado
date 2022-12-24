import random

def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        print('Opção Inválida...Tente Novamente:')
        x = int(input(pergunta))
    return x


notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
cont = 0
for nota in notas:
    if nota == 7:
        cont += 1
print(notas)
print(cont)
print(notas.count(7))
notas.append(4)
notas.pop()
notas.sort()
print(notas)
soma = 0
len(notas)
for nota in notas:
    soma += nota
print(soma)
print(soma / len(notas))

for nota in notas:
    maior = 0
    if nota > maior:
        maior += nota
        print(notas)
        print(maior)

palavras = ('Jose', 'Mario', 'Sergio', 'Marcos', 'Roberto')
for palavra in palavras:
    print('\nPalavra:{}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')


def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:  # Pedra
        if jogador2 == 1:  # Pedra
            empate += 1

        elif jogador2 == 2:  # Papel
            v2 += 1

        elif jogador2 == 3:  # Tesoura
            v1 += 1

    elif jogador1 == 2:  # Papel
        if jogador2 == 1:  # Pedra
            v1 += 1

        elif jogador2 == 2:  # Papel
            empate += 1

        elif jogador2 == 3:  # Tesoura
            v2 += 1

    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1

        elif jogador2 == 2:  # Papel
            v1 += 1

        elif jogador2 == 3:  # Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados


# Programa Principal
print('JOKEMPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Resultados e Sair')
resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = validacao('EScolha sua Jogada:'
                   '1 = Pedra\t'
                   '2 = Papel\t'
                   '3 = Tesoura\t'
                   '0 = Finalizar jogos\t', 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)
    # print(vencedor(j1,j2))
    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Numero de vitorias do jogador 1 :{}'.format(resultados[0]))
print('Numero de vitorias do jogador 2 :{}'.format(resultados[1]))
print('Numero de empates :{}'.format(resultados[2]))

cadastro = {'Nome': [],
            'Sexo': [],
            'Ano': []}
while True:
    terminar = input('Deseja cadastrar uma pessoa ? [S/N]'.upper())
    if terminar =='N':
        print('Programa encerrado....\n')
        break
    if  terminar == 'S':
        print('Digite S para sim ou N para não')
        nome = input('Qual o seu nome ?')
        sexo = input('Qual o seu sexo ?[M/F]')
        ano = int(input('Qual o ano de seu nascimento ?'))
        cadastro['Nome'].append(nome)
        cadastro['Sexo'].append(sexo.upper())
        cadastro['Ano'].append(ano)


print(cadastro)