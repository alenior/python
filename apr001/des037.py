num = int(input('Informe um número inteiro para convertê-lo para outra base numérica: '))
base = int(input('Escolha a base numérica para converter o número {}: (0: Binário; 1: Octal; 2: Hexadecimal) '.format(num)))

if base == 0:
    print('O número {} em binário é: {}.'.format(num, bin(num)))
elif base == 1:
    print('O número {} em octal é: {}.'.format(num, oct(num)))
elif base == 2:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Opção inválida. Encerrando programa.')
