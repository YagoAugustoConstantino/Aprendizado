def contorno(s1):
    tam = len(s1)
    print('+', '-' * tam, '+')
    print('+', '-' * tam, '+')
    print('|', s1, '|')
    print('+', '-' * tam, '+')
    print('+', '-' * tam, '+')
    return s1


contorno('Te Amo Yenny')


def soma(x, y):
    res = x + y
    print(res)
    return res


soma(75, 85)


def media_de_velocidade():
    x = int(input('quantos kilometros foram percorridos?'))
    y = int(input('em quantas horas ?'))
    z = x/y
    print('a média de velocidade foi de %.2f KM/H'%z)
    return z

media_de_velocidade()


