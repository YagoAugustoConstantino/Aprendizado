idade=int(input('qual a sua idade' ))
if idade >18:
    print('entrada permitida para quem tem {} anos'.format(idade))
if idade <18:
    print('entrada negada para quem tem {} anos'.format(idade))
x = int(input('digite um numero inteiro:'))
y = int(input('digite outro numero inteiro:'))
print('a soma de {} com {} é igual a {}'.format(x, y, x+y))
print('a soma de %i com %i é igual a %i' % (x, y, x+y))
z=int(input('quantos kilometros vc rodou?'))
f=int(input('quantos dias vc alugou o carro ?'))
print('o preço a pagar é {}'.format(f*60+z*0.15))
