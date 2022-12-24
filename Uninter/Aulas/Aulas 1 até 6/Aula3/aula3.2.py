print('veja nossa oferta de frutas ')
print('1  Maça//2,30 R$')
print('2 Laranja//3,60 R$')
print('3 Banana//1,85 R$')
fruta = int(input('qual fruta voce deseja?'))
if fruta==1:
    print('escolheu maça')
elif fruta ==2:
    print('esolheu laranja')
elif fruta==3:
    print('escolheu banana')
qtd = int(input('quantas frutas ?'))
if fruta == 1:
    print('voce comprou {} maças , o preço fica {} reais'.format(qtd, qtd * 2.3))
elif fruta == 2:
    print('voce comprou {} laranjas , o preço fica {} reais'.format(qtd, qtd * 3.6))
elif fruta == 3:
    print('voce comprou {} Bananas , o preço fica {} reais'.format(qtd, qtd * 1.85))
else:
    print('não tem,os esse produto')
nome = input('qual o seu nome')
idade = int(input('qual a sua idade'))
if nome == 'Vinicius':
    print('esse é o Vinicius')
elif idade >= 18 and idade < 100:
    print('{} tem {} anos e é maior de idade'.format(nome, idade))
elif idade <= 18 and idade < 100:
    print('{} tem {} anos e é menor de idade'.format(nome, idade))
elif idade > 100:
    print('essa pessoa provavelmente nao existe')
n1 = int(input('escolha um numero'))
n2 = int(input('escolha outro numero'))
print('Calculadora')
print(' 1 adição +')
print('2 subtração -')
print('3 multiplicação*')
print('4 divisão - ')
operacao = int(input('qual operação voce deseja fazer ? '))
if operacao == 1:
    print('{}+{}={}'.format(n1, n2, n1 + n2))
elif operacao == 2:
    print('{}-{}={}'.format(n1, n2, n1 - n2))
elif operacao == 3:
    print('{}*{}={}'.format(n1, n2, n1 * n2))
elif operacao == 4:
    print('{}/{}={}'.format(n1, n2, n1 / n2))
else:
    print('imposivel fazer essa operacão')

print('tipos de estabelecimentos')
print('1 Residencial')
print('2 Comercial')
print('3 industrial')
tipo = int(input('qual o tipo do seu estabelecimeno'))
quantos_kwh = int(input('quanto é gasto de energia?'))
if tipo == 1 and quantos_kwh <= 500:
    print('o preço a se pagar pela energia eletrica é de {} reais'.format(quantos_kwh * 0.4))
elif tipo == 1 and quantos_kwh > 500:
    print('o preço a se pagar pela energia eletrica é de {} '.format(quantos_kwh * 0.65))
elif tipo == 2 and quantos_kwh <= 1000:
    print('o preço a se pagar pela energia elétrica é de {} reais'.format(quantos_kwh * 0.55))
elif tipo == 2 and quantos_kwh > 1000:
    print('o preço a se pagar pela energia eletrica é de {} reais'.format(quantos_kwh * 0.6))
elif tipo == 3 and quantos_kwh <= 5000:
    print('o preço a se pagar pela energia elétrica é igual a {} reais'.format(quantos_kwh * 0.55))
elif tipo == 3 and quantos_kwh > 5000:
    print('o preço a se pagar pela energia elétrica é igual a {} reais'.format(quantos_kwh * 0.6))
else:
    print('fora da tabela de preços')
