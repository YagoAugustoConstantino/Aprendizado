def ExixteArquivo1(nomearquivo):
    global x
    try:
        with open(nomearquivo, 'rt') as x:
            x.read()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo1(nomearquivo):
    global x
    try:
        with open(nomearquivo, 'wt+') as x:
            x.write(' ')

    except:
        print('Erro na criação de arquivo')
    else:
        print(f'Arquivo {nomearquivo} foi criado com sucesso')


def EscreverArquivo(nomearquivo):
    try:
        with open(nomearquivo, 'at+') as x:
            x.write(input('insira o que será escrito no arquivo'))
            x.write('\n')
    except:
        print('Não foi possivel abrir o arquivo')


def lerarquivocompleto1(nomearquivo):
    try:
        with open(nomearquivo, 'rt+') as x:
            print(x.read())
    except:
        print('Não foi possivel abrir o arquivo')


def cadastrarjogo(nomearquivo, nomeJogo, nomeVideogame):
    global x
    try:
        x = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        x.write(f'{nomeJogo}:{nomeVideogame}\n')
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



                                    # criarArquivo1('NotasNovas')
EscreverArquivo('NotasNovas')
listarArquivo('NotasNovas')
#listarArquivo('../ARQUIVOS/notas2.txt')
