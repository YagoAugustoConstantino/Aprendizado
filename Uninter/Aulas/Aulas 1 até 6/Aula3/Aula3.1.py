x = [15, 3, 65, 9, 78, 35, 12, 33]
print(sorted(x))
print(7 // 3)
print(2 ** 2 + 3 ** 2)
print(1387 / 19)
ano = int(input('um ano'))
if ano % 4 == 0:
    print('esse ano pode ser bissexto')
else:
    print('esse ano não é bissexto')
A = float(input('lado1 do triangulo'))
B = float(input('lado2 do triangulo'))
C = float(input('lado3 do triangulo'))
if A > 0 and B > 0 and C > 0:
    if (A + B > C) and (B + C > A) and (C + A > B):
        print('é um triangulo')
    elif A  == B == C:
        print('é um triangulo equilátero')
    elif A == B or B == C or C == A:
        print('é um triangulo escaleno')
    elif A != B or B != C or C != A:
        print('é um triangulo escaleno')
    else:print('não é um triangulo')

    a=open('../games.txt', 'wt+')
    a.write('{};{}\n'.format(54,75))
    a.close()
