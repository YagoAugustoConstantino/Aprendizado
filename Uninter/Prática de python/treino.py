from math import sqrt
print(sqrt(9))
notas = [9,7,7,10,3,9,6,6,2]

print(notas.count(7))

notas.pop()

notas.append(4)

print(notas)

palavras = ('Mario','Luigi','Peach','Yoshi','Bowser')
for palavra in palavras:
    print(f'\nPalavra:{palavra.upper()} // Vogais:',end=' ' )
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(),end=' ')

