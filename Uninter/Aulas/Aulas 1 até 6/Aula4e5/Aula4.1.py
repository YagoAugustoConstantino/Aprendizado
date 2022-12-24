soma = 0 #uso de while
cont = 1
while cont <= 5:
    x = float(input('insira a sua {} nota'.format(cont)))
    soma += x
    cont += 1
print('a media de notas foi de %2.f' % (soma / 5))
#validar entrada
print('insira um valor inteiro e positivo para encerrar o programa')
x = int(input('insira o valor'))
while x <= 0:
    if x <= 0:
        print('esse valor é invalido')
        x = int(input('insira o valor'))
print('valor aceitável///encerrando o programa')
#exercicio com string
f=input('insira uma palavra ')
print('para encerrar o programa digite sair')
while f!= 'sair':
    print(f)
    f = input('insira uma palavra ')

print('programa encerrado')

print('insira uma palavra e ela será repetida')
print('para sair do programa digite sair')
while True:
    texto=input('')
    print(texto)
    if texto == 'sair':
        break
print('programa encerrado')

print('coloque um login')
print('coloque senha')
while True:
    login=input('qual o login ?')
    if login != 'yago':
        continue
    senha=input('qual a senha?')
    if senha == 'yenny':
        break
print('programa encerrado' )
#falsey and truthy
nome=''
while not nome:
    nome=input('coloque um nome')
valor=int(input('insira um numero'))
if valor>0:
    print('numero positivo')
else:
    print('numero negativo')


for i in range (5):
    i+=1
    print(i)

soma=0
qtd=0
for i in range (1,101):
    if i %2==0:
        soma+=i
        qtd+=1
media=soma/qtd
print('a media dos numeros pares de 1 a 100 é de {}'.format(media))
