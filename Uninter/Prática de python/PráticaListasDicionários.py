arquivo = 'Games.txt'
def validacao(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        print('Opção Inválida...Tente Novamente:')
        x = int(input(pergunta))
    return x

def ExixteArquivo(nomearquivo):
    try:
        x = open(nomearquivo, 'rt')
        x.close()
    except FileNotFoundError:
        return False
    else:
        return True
        # Programa Principal


def criarArquivo(nomearquivo):
    try:
        x = open(nomearquivo, 'wt+')
        x.close()
    except:
        print('Erro na criação de arquivo')
    else:
        print(f'Arquivo {nomearquivo} foi criado com sucesso')


def cadastrarjogo(nomearquivo, nomeJogo, nomeVideogame):
    global x
    try:
        x = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        x.write(f'Titulo:{nomeJogo}//VideoGame:{nomeVideogame}\n')
    finally:
        x.close()


def listarArquivo(nomearquivo):
    global x
    try:
        x = open(nomearquivo, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        print(x.read())
    finally:
        x.close()

if ExixteArquivo(arquivo):
    print('Arquivolocalizado')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastras produtos')
    print('2 - Listar produtos')
    print('3 - Sair')
    op = validacao('Escolha a opção desejada', 1, 3)
    if op == 1:
        print('Cadastrar itens selecionado...\n')
        nomejogo = input('Qual o nome do jogo ?')
        nomevideogame = input('Qual o nome do videogame?')
        cadastrarjogo(arquivo, nomejogo, nomevideogame)


    elif op == 2:
        print('Listar produtos seleionada ... \n')
        listarArquivo(arquivo)


    elif op == 3:
        print('Encerrando programa...\n')
        break
