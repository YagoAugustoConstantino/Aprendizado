def contorno(s1):
    tam = len(s1)
    print('+', '-' * tam, '+')
    print('|', s1, '|')
    print('+', '-' * tam, '+')
    return s1

operacao=0
while True:
    print('\n')
    n1 = (int(input('Insira um número ')))
    n2 = (int(input('Insira um  segundo número ')))
    print('\n')
    contorno('Calculadora')
    contorno(' + Adição = 1 ')
    contorno(' - Subtração = 2 ')
    contorno(' * Multiplicação = 3 ')
    contorno(' / Divisão = 4 ')
    contorno(' Para sair digite s')
    print('\n')
    operacao = (input('Qual operação deseja Fazer?\n'))
    if operacao == 1:
        print('{}+{}={}'.format(n1, n2, n1 + n2))
    elif operacao == 2:
        print('{}-{}={}'.format(n1, n2, n1 - n2))
    elif operacao == 3:
        print('{}*{}={}'.format(n1, n2, n1 * n2))
    elif operacao == 4:
        print('{}/{}={}'.format(n1, n2, n1 / n2))
    elif operacao == 's':
        break
    else:
        print('Impossivel fazer essa operacão')
        print('\n')
    continue

inicial=int(input('Insira um número para saber sua tabuada'))
tabuada=int(input('Até qual tabuada do numero vc deseja saber'))
x=0
while x < tabuada:
    x+=1
    print(f' a Tabuada de {inicial} X {x} é igual a : {inicial*x} ')
