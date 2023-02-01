def contador(*num):
    soma = 0
    tam = len(num)
    for item in num:
        soma += item
    print(f'Recebi os valores {num} , ao total sao {tam} Números, e a soma total é de {soma} \n')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def contagem(i, f, p):
    if p < 0:
        p *= -1
    if i < f:
        while i <= f:
            print(i, end=' ')
            i += p
    elif i > f:
        while i >= f:
            print(i, end=' ')
            i -= p


x = [1, 2, 3, 5]

dobra(x)
print(x)
contador(1, 2, 3, 4, 5, 6, 7)
contador(7, 2, 6)
contador(5, 6, 9, 7)
contagem(1, 10, 1)
contagem(1, 10, 2)
contagem(1, 20, 5)
contagem(10, 0, 2)
