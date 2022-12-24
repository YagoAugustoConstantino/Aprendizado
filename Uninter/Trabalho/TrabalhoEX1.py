
print('Bem vindo a loja de Yago Costantino')  # Aluno:Yago Constantino RU:4206622
Valor_do_produto = float(input('Qual o valor do produto?'))
qtd_do_produto = int(input('Quantos produtos você deseja?'))
Valor_total = Valor_do_produto * qtd_do_produto
if Valor_do_produto <= 4:  # Em compras de menos de 5 produtos Não damos desconto
    print('O valor a se pagar é {} reais'.format(Valor_total))
elif Valor_do_produto > 5 < 20:  # Em compras entre 5 e 19 produtos damos 3% de desconto
    desconto = Valor_total - (Valor_total * 0.03)
    print('O valor sem desconto é de {} reais'.format(Valor_total))
    print('O valor com desconto é de {} reais'.format(desconto))
elif Valor_do_produto > 20 < 100:  # Em compras entre 20 e 99 produtos damos 6% de desconto
    desconto = Valor_total - (Valor_total * 0.06)
    print('O valor sem desconto é de {} reais'.format(Valor_total))
    print('O valor com desconto é de {} reais'.format(Valor_total - desconto))
elif Valor_do_produto >= 100:  # Em compras acima de 100 produtos damos 10 % de desconto
    desconto = Valor_total - (Valor_total * 0.1)
    print('O valor sem desconto é de {} reais'.format(Valor_total))
    print('O valor com desconto é de {} reais'.format(Valor_total - desconto))
else:
    print('Nossa Loja não trabalha com esse produto nessa quantidade')



