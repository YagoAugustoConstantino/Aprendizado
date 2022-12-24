while True:
    codigo = int(input('coloque um numero'))
    if 19 < codigo < 26:
        break
    else:
        print('codigo invalido')
        continue
tabuada = 1
while tabuada <= 10:
    print('Tabuada do {}'.format(tabuada))
    n = 1
    while n <= 10:
        print('{}X{} é igual a {}'.format(tabuada, n, tabuada * n))
        n += 1
    tabuada += 1
# Usando For
for tabuada in range(1, 11, 1):
    print('Tabuada do {}'.format(tabuada))
    for i in range(1, 11, 1):
        print('{}X{} = {}'.format(tabuada, i, tabuada * i))
for i in range(3, 13, 1):
    print(i)

i = 0
while i < 9:
    i += 2
    print(i)

while True:
    n1 = int(input('escolha um numero'))
    n2 = int(input('escolha outro numero'))
    print('escolha qual operação deseja fazer:'
          '1 Adição // 2 Subtração // 3 Multiplicação // 4 Divisão// 5 Sair // ')
    op = int(input(''))

    if op == 1:
        print('{}+{}={}'.format(n1, n2, n1 + n2))
        continue
    elif op == 2:
        print('{}-{}={}'.format(n1, n2, n1 - n2))
        continue
    elif op == 3:
        print('{}*{}={}'.format(n1, n2, n1 * n2))
        continue
    elif op == 4:
        print('{}/{}={}'.format(n1, n2, n1 / n2))
        continue
    elif op == 5:
        print('programa encerrado')
        break
v = int(input('qual valor deseja sacar em R$?'))
while True:
    if v >= 100:
        ced100 = v // 100
        v -= (ced100 * 100)
        print('{} Cedulas de 100 '.format(ced100))
        if not v:
            break
    if v >= 50:
        ced50 = v // 50
        v -= (ced50 * 50)
        print('{} Cedulas de 50 '.format(ced50))
    if not v:
        break
    if v >= 20:
        ced20 = v // 200
        v -= (ced20 * 20)
        print('{} Cedulas de 20 '.format(ced20))
    if not v:
        break
    if v >= 10:
        ced10 = v // 10
        v -= (ced10 * 10)
        print('{} Cedulas de 10 '.format(ced10))
    if not v:
        break
    if v >= 5:
        ced5 = v // 5
        v -= (ced5 * 5)
        print('{} Cedulas de 5 '.format(ced5))
    if not v:
        break
    if v:
        ced1 = v
        print('{} Cedulas de 1 '.format(ced1))
    break

while True:
    idade =(input('qual a sua idade'))
    numero_de_pessoas = 0
    media_de_idade = 0
    preco_dos_ingressos = 0
    if idade == 'sair':
        break
    idade=int(idade)
    if idade <=3:
        ingresso=0


