import time

soma = 0
for i in range(0, 3):
    x = int(input('Insira 3 numeros para descobrir sua soma'))
    soma += x

print(soma)
cont = 0
print('\n \n')
while cont <= 5:
    print (cont)
    cont+=1
    print('\n')

for i in range(3,13):
    print (i)
    print('\n \n')
contagem=3
while contagem <=12:
    print(contagem)
    contagem += 1
    print('\n\n')

for i in range(0,10,2):
    print(i)

print('\n\n')

contador=0
while contador <=9:
    print(contador)
    contador +=2

print('\n')

def calculadora():
    while True:
        n1 = float(input('Insira o Primeiro Número\n'))
        n2 = float(input('Insira o Segunda Número\n'))
        op = int(input('''Digite 1 para Somar os Números:
Digite 2 para Subtrair os Números:
Digite 3 para Multiplicar os Números:
Digite 4 para Dividir os Números :
Digite 5 Para Sair'''))
        if op ==1:
            print(f'A Soma do Primeiro com o Segundo Número é {n1+n2}')
        elif op ==2:
            print(f'A Subtração  do Primeiro com o Segundo Número é {n1 - n2}')
        elif op == 3:
            print(f'A Multiplicação do Primeiro com o Segundo Número é {n1 * n2}')
        elif op == 4:
            print(f'A Divisão do Primeiro com o Segundo Número é {n1 / n2}')
        elif op == 5 :
            print('Encerrando o Programa... ')
            time.sleep(2)
            break
        elif op not in range(0,6):
            print('Opção Inválida ... Tente novamente')
            continue

calculadora()