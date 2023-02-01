matriz = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0]]
spar = 0
scol1 = 0
scol2 = 0
scol3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para posição [{linha, coluna}] '))
        if matriz[linha][coluna] == matriz[linha][2]:
            scol3 += matriz[linha][2]
        elif matriz[linha][coluna] == matriz[linha][1]:
            scol2 += matriz[linha][1]
        elif matriz[linha][coluna] == matriz[linha][0]:
            scol1 += matriz[linha][0]

for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:5^}]', end='')
    print('')
print('-=' * 30)

for l in matriz:
    for c in l:
        if int(c) % 2 == 0:
            spar += c

print(spar)
print(scol3)
print(scol2)
print(scol1)
