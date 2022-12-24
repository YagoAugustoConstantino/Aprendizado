salario = float(input('qual o seu salario?'))
ano_de_admissao = int(input('em que ano entrou na empresa ?'))
ano_atual = int(input('qual o ano atual?'))
tempo = ano_atual - ano_de_admissao
if tempo > 10:
    bonus = salario * 0.3
elif tempo > 5:
    bonus = salario * 0.2
elif tempo < 5:
    bonus = salario * 0.1
print('voce tem %s anos na empresa' % tempo)
print('seu salario é de {} reais'.format(salario))
print('seu bonus é de{}reais'.format(bonus))
print('seu salario final é de {} reais'.format(salario + bonus))
if 1387 % 19 == 1:
    print('é divisivel')
else:
    print('não é divisivel')
if 31 % 2:
    print('é par')
else:
    print('não é par')
idade = int(input('qual a sua idade?'))
if idade > 60:
    print('voce tem direito a aposentadoria')
else:
    print('voce não tem direito a aposentadoria')
dano = int(input('quantidade de dano'))
if dano > 10:
    print('escudo atravessado')
else:
    print('dano segurado pelo escudo')
ano = int(input('em que ano estamos?'))
if ano / 4 > 1:
    print('pode ser um ano bissexto')
else:
    print('não é bissexto')
lado1: int = int(input('qual o tamonho do primeiro lado do triangulo?'))
lado2 = int(input('qual o tamonho do segundolado do triangulo?'))
lado3 = int(input('qual o tamonho do terceiro lado do triangulo?'))
if lado1 == lado2 and lado2 == lado3:
    print('triangulo equilatero')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('triangulo isoceles')
else:
    print('triangulo escaleno')
residencial = int(input('quantos kwh gasto na residencia?'))
comercial = int(input('quantos kwh gasto no comercio?'))
industria = int(input('quantos kwh gasto na industria?'))
if residencial > 500:
    precoresidencial = residencial * 0.4
elif residencial < 500:
    precoresidencia = residencial * 0.55
if comercial < 1000:
    precocomercial = comercial * 0.55
elif comercial > 1000:
    precocomercial = comercial * 0.6
if industria < 5000:
    precoindustria = industria * 0.50
elif industria > 5000:
    precoindustria = industria * 0.40
