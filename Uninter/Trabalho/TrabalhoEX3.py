# Aluno Yago Augusto Constantino Ribeiro RU:4206622
def Menu_Volume():  # Função Volume onde irá retornar um valor
    print('MENU VOLUME')
    volume = int(input('A quantidade que deseja da Feijoada(ML)'))
    try:  # try para caso seja digitado character
        volume
    except ValueError:
        print('A Resposta para Volume é inválida...Tente um Número')
    while True:
        if volume < 300 or volume > 5000:  # condicional para fora do aceitável
            print('Opção de MLs Inválida...Tente Novamente')
            volume = int(input('A quantidade que deseja da Feijoada(ML)\n'))
        else:
            print('A opção de {} Mls é válida'.format(volume))
            print('O Valor a se pagar é de {} R$'.format(volume * 0.08))
            return volume * 0.08


def Menu_Feijoada():  # Função feijoada retornará um multiplicador para a conta final
    print('|___________________MENU FEIJOADA_________________|')
    print('|____Tipo____|____Descrição__________|___Preço____|')
    print('| b = Básica |Feijão+Paiol+Costelinha|     1.00X  |')
    print('|-------------------------------------------------|')
    print('| p = Premium|Feijão+Paiol+Costelinha|     1.25X  |')
    print('|            +Partes do porco                     |')
    print('|-------------------------------------------------|')
    print('|s= Suprema |Feijão+Paiol+Costelinha|      1.50X  |')
    print('|           +Partes do Porco+Charque              |')
    print('|           +Calabresa + Bacon                    |')
    while True:
        Feijoada = input('Qual opção de Feijoada Você deseja?:\n')
        if Feijoada == 'b':
            print('Você selecionou a feijoada Básica')
            print('o Multiplicador da feijoada será de 1.00X em Relação ao Volume')
            return 1
        elif Feijoada == 'p':
            print('Você selecionou a feijoada Premium')
            print('o Multiplicador da feijoada será de 1.25X em Relação ao volume')
            return 1.25
        elif Feijoada == 's':
            print('Você selecionou a feijoada Suprema')
            print('o Multiplicador da feijoada será de 1.50X')
            return 1.5
        elif Feijoada != 'b' or Feijoada != 'p' or Feijoada != 's':
            print('Opção de Feijoada inválida...Tente novamente')
            continue
        break


def Menu_Acompanhamento():
    # função acompanhamneto retornará uma soma para o valor final
    print('|________________Menu_Acompanhamento______________|')
    print('|_Código-|_____Acompanhamento_____|_____Preço_____|')
    print('|    0   |Não quero Acompanhamento|     0.00 R$    ')
    print('|    1   | 200g de Arroz          |     5.00 R$    ')
    print('|    2   | 150g de Farofa especial|     6.00 R$    ')
    print('|    3   | 100g de Couve cozida   |     7.00 R$    ')
    print('|    4   | 1 Laranja descascada   |     3.00 R$    ')
    Valor_acompanhamento = 0  # somador do valor
    while True:
        Acompanhamento = int(input('Qual o Código do seu Acompanhamento?\n'))
        if Acompanhamento == 0:
            print('Não deseja acompanhamento')
            Valor_acompanhamento += 0
            break
        elif Acompanhamento == 1:
            print('Você adquiriu um Acompanhamento de Arroz pelo Valor de 5.00 R$\n')
            Valor_acompanhamento += 5
        elif Acompanhamento == 2:
            print('Você adquiriu um Acompanhamento de Farofa Especial pelo Valor de 6.00 R$\n')
            Valor_acompanhamento += 6
            print('O Preço a se pagar atual é igual a {} R$'.format(Valor_acompanhamento))
        elif Acompanhamento == 3:
            print('Você adquiriu um Acompanhamento de Couve Cozida pelo Valor de 7.00 R$\n')
            Valor_acompanhamento += 7
            print('O Preço a se pagar atual é igual a {} R$'.format(Valor_acompanhamento))
        elif Acompanhamento == 4:
            print('Você adquiriu um Acompanhamento de Laranja descascada pelo Valor de 3.00 R$\n')
            Valor_acompanhamento += 3
            print('O Preço a se pagar atual é igual a {} R$'.format(Valor_acompanhamento))
        elif Acompanhamento < 0 or Acompanhamento > 4:
            print('Código inválido .. Tente novamente')
            continue
        pergunta = int(input('Deseja mais acompanhamentos?///1=sim///0=não'))
        if pergunta == 1:
            continue
        else:
            break
    return Valor_acompanhamento  # retorno final do acompanhamento


print('Bem vindo A Cozinha do Yago Constantino RU:4206622\nHoje servirmos Feijoada')  # Yago Constantino RU:4206622
valorvolume = Menu_Volume()
valorfeijoada = Menu_Feijoada()
valoracompanhamento = Menu_Acompanhamento()
print('O Valor Final é de {} R$'.format((valorvolume * valorfeijoada) + valoracompanhamento))
from TrabalhoEX4 import Cadastrar_produto
Cadastrar_produto(1)