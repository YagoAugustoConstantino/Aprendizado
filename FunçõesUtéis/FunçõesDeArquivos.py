import os

lista_de_arquivos = os.listdir(r'..\ARQUIVOS')
for arquivo in lista_de_arquivos:
    print(arquivo)


def exixtearquivo1(nomearquivo):
    try:
        with open(nomearquivo, 'rt') as doc:
            doc.read()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo1(nomearquivo):
    try:
        with open(nomearquivo, 'wt+') as doc:
            doc.write(' ')

    except FileNotFoundError:
        print('Erro na criação de arquivo')
    else:
        print(f'Arquivo {nomearquivo} foi criado com sucesso')


def escreverarquivo(nomearquivo):
    try:
        with open(nomearquivo, 'at+') as doc:
            doc.write(input('insira o que será escrito no arquivo'))
            doc.write('\n')
    except FileNotFoundError:
        print('Não foi possivel abrir o arquivo')


def lerarquivocompleto1(nomearquivo):
    try:
        with open(nomearquivo, 'rt+') as doc:
            print(doc.read())
    except FileNotFoundError:
        print('Não foi possivel abrir o arquivo')


def cadastrarjogo(nomearquivo, nomejogo, nomevideogame):
    try:
        with open(nomearquivo, 'at') as doc:
            doc.write(f'{nomejogo}:{nomevideogame}\n')
    except FileNotFoundError:
        print('Erro ao abrir arquivo')
    else:
        print('Cadastro Bem sucedido')


def listararquivo(nomearquivo):
    global arquivo
    try:
        arquivo = open(nomearquivo, 'rt')
    except FileNotFoundError:
        print('Erro ao abrir o arquivo')
    else:
        print(arquivo.read())
    finally:
        arquivo.close()
# criararquivo1('NotasNovas')
# escreverarquivo('NotasNovas')
# listararquivo('NotasNovas')
# listarArquivo('../ARQUIVOS/notas2.txt')
