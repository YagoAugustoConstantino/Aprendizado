def soma(x=0, y=0, z=0):
    """
    função que soma até 3 numeros opcionais
    :param x:valor inteiro opcional
    :param y:valor inteiro opcional
    :param z:valor inteiro opcional
    :return:a soma dos valores//x+y+z
    """
    return x + y + z


print(soma(5, 6))


def valida(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i  # fat=fat*i
    return fat


x = valida('insira um numero positivo e inteiro para saber a fatorial', 0, 9999)

print('o fatorial de {} é igual a {}'.format(x, (fatorial(x))))


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



def cadastrarjogo(nomearquivo,nomejogo,nomevideogame):
    global a
    try:
        a=open(nomearquivo,'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo,nomevideogame))
    finally:
        a.close()

def listararquivo(nomearquivo):
    try:
        a=open(nomearquivo,'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print((a.read()))
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
        nomejogo=input('Nome do jogo ')
        nomevideogame=input('Nome do video game')
        cadastrarjogo=(arquivo,nomejogo,nomevideogame)
    elif op == 2:
        print('Opção Listagem selecionada....\n')
        listararquivo(arquivo)

    elif op == 3:
        print('Encerrando programa')
        break
