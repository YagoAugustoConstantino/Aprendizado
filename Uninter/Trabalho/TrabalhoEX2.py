# Bem vindo a Pizzaria de Yago Constantino     RU:4206622
print('----------------------Cardápio---------------------')
print('\033[4:34mCódigo |    Sabor    | Pizza Média | Pizza Grande |')
print('   21  | Napolitana  |     R$20,00 |      R$26,00 |')
print('   22  | Margherita  |     R$20,00 |      R$26,00 |')
print('   23  | Calabresa   |     R$25,00 |      R$32,50 |')
print('   24  | Toscana     |     R$30,00 |      R$39,00 |')
print('   25  | Portuguesa  |     R$30,00 |      R$39,00 |')
precofinal = 0
while True:
    tam = input('Qual o tamanho da pizza desejada ?// M / G  '.upper())
    codigo = int(input('Qual o codigo do sabor da pizza desejada ?'))
    if codigo == 21 and   tam == 'M':
        print('Você comprou uma pizza Napolitana Média')
        preco = 20
        precofinal += 20  # calculo do preço total da compra
    elif codigo == 21 and tam == 'G' :
        print('Você comprou uma pizza Napolitana Grande')
        preco = 26
        precofinal += 26
    elif codigo == 22 and tam == 'M':
        print('Você comprou uma pizza Margherita Média')
        preco = 20
        precofinal += 20
    elif codigo == 22 and tam == 'G':
        print('Você comprou uma pizza Margherita Grande')
        preco = 26
        precofinal += 26
    elif codigo == 23 and tam == 'M' :
        print('Você comprou uma pizza Calabresa Média')
        preco = 25
        precofinal += 25
    elif codigo == 23 and tam == 'G':
        print('Você comprou uma pizza Calabresa Grande')
        preco = 32.5
        precofinal += 32.5
    elif codigo == 24 and tam == 'M':
        print('Você comprou uma pizza Toscana Média')
        preco = 30
        precofinal += 30
    elif codigo == 24 and tam == 'G':
        print('Você comprou uma pizza Toscana Grande')
        preco = 39
        precofinal += 39
    elif codigo == 25 and tam == 'M':
        print('Você comprou uma pizza Portuguesa Média')
        preco = 30
        precofinal += 30
    elif codigo == 25 and tam == 'G':
        print('Você comprou uma pizza Portuguesa Grande')
        preco = 39
        precofinal += 39
    elif 25 > codigo < 20 or tam != 'M' or tam != 'G':  # Caso tamanho ou código inválido recomeçar o programa
        print('Opção inválida')
        continue
    pergunta = int(input('Deseja pedir mais alguma coisa ? Sim=1/Não=0'))
    if pergunta == 0:
        print('o Valor final a se pagar é de {} R$'.format(precofinal))
        break
    else:
        print('o valor atual a se pagar é de {} R$'.format(precofinal))
        continue
