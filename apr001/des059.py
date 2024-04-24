num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
opcao = int(input('Qual operação deseja fazer com eles? [1: SOMA | 2: MULTIPLICAÇÃO | 3: DEFINIR O MAIOR | 4: INFORMAR '
                  'NOVOS NÚMEROS | 5: SAIR DO PROGRAMA]: '))
while opcao in range(1, 5):
    if opcao == 1:
        print('A soma de {} e {} é {}.'.format(num1, num2, num1 + num2))
        opcao = int(input('Qual operação deseja fazer com eles? [1: SOMA | 2: MULTIPLICAÇÃO | 3: DEFINIR O MAIOR | 4: '
                          'INFORMAR'
                  'NOVOS NÚMEROS | 5: SAIR DO PROGRAMA]: '))
    elif opcao == 2:
        print('A multiplicação de {} por {} dá {}.'.format(num1, num2, num1 * num2))
        opcao = int(
            input('Qual operação deseja fazer com eles? [1: SOMA | 2: MULTIPLICAÇÃO | 3: DEFINIR O MAIOR | 4: INFORMAR '
                  'NOVOS NÚMEROS | 5: SAIR DO PROGRAMA]: '))
    elif opcao == 3:
        print('O maior número entre {} e {} é o {}.'.format(num1, num2, max(num1, num2)))
        opcao = int(
            input('Qual operação deseja fazer com eles? [1: SOMA | 2: MULTIPLICAÇÃO | 3: DEFINIR O MAIOR | 4: INFORMAR '
                  'NOVOS NÚMEROS | 5: SAIR DO PROGRAMA]: '))
    else:
        num1 = int(input('Informe um novo número: '))
        num2 = int(input('Informe outro novo número: '))
        opcao = int(
            input('Qual operação deseja fazer com eles? [1: SOMA | 2: MULTIPLICAÇÃO | 3: DEFINIR O MAIOR | 4: INFORMAR '
                  'NOVOS NÚMEROS | 5: SAIR DO PROGRAMA]: '))
print('Você escolheu sair! Fim de programa.')
