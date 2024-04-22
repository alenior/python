precoNormal = float(input('Informe o preço do produto (R$): '))
condicao = int(input('Informe a condição de pagamento (0: à vista dinheiro/cheque (10% desconto); 1: à vista cartão ('
                     '5% desconto); 2: 2x no cartão (preço normal); 3: 3x ou + no cartão (20% de acréscimo): '))
if condicao == 0:
    print('Valor a pagar: R$ {}.'.format(precoNormal * 0.9))
elif condicao == 1:
    print('Valor a pagar: R$ {}.'.format(precoNormal * 0.95))
elif condicao == 2:
    print('Valor a pagar: R$ {}.'.format(precoNormal))
elif condicao == 3:
    print('Valor a pagar: R$ {}.'.format(precoNormal * 1.2))
else:
    print('Condição inválida! Impossível determinar valor a pagar. Encerrando agora.')
