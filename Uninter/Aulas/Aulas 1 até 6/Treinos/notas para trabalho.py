def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('Opção Inválida...Tente Novamente:')
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso'.format(nomedoarquivo))


def cadastrarjogo(nomearquivo, nomejogo, nomevideogame):
    global a
    try:
        a = open(nomearquivo, 'at')
        a.write('{};{}\n'.format(nomejogo, nomevideogame))
    finally:
        a.close()


def listararquivo(nomearquivo):
    global a
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo Inexistente ')

criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar item')
    print('2 - listagem dos cadastros')
    print('3 - Encerrar programa')
    op = validacao('Escolha a opção desejada', 1, 4)
    if op == 1:
        print('Opção de Cadastrar novo item selecionada....\n')
        nomedojogo = input('Nome do jogo ')
        nomedovideogame = input('Nome do video game')
        cadastrarjogo = ('games.txt', nomedojogo, nomedovideogame)
    elif op == 2:
        print('Opção Listagem selecionada....\n')
        listararquivo('games.txt')

    elif op == 3:
        print('Encerrando programa')
        break

