idade = input('qual sua idade')
print(idade)
ano = 'o ano no qual voce nasceu'
print(len(ano))
print(704 // 4)
print(2 ** 10)
print(abs(54 - 57))
print(min(34, 29, 31))
a = int(3)
b = 4
c = a * a + b * b
print(a, b, c)
a1 = 'ant'
a2 = 'bat'
a3 = 'cod'
print(a1, a2, a3)
print(a1 * 10)
print(a1, a2 * 2, a3 * 3)
print((a1 + ' ' + a2) * 10)
print((a2 + ' ' + a2 + ' ' + a3) * 5)
preco = float(input('valor do produto'))
p = float(input('percentual de desconto  0 a 100%:'))
desconto = preco * (p / 100)
precofinal = preco - desconto
print('o desconto sera de {} reais ,totalizando {} % de desconto portanto o preço final será de {}'.format(desconto, p,
                                                                                                           precofinal))
print((256 / 100) * 12)
km = int(input('quantos quilometros rodados?'))
dias = int(input('quantos dias alugado? '))
preco2 = km * 0.15 + dias * 60
preco3 = km * 0.15
preco4 = dias * 60
print(
    'o preço a se pagar é de {} baseado nos {} dias e nos {} quilometros rodados no qual o custo por quilometragem '
    'foi de {} reais e o preco por aluguel foi de {} reais '.format(
        preco2, dias, km, preco3, preco4))
