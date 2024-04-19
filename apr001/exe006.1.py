num = int(input('Informe um número: '))
print('Você informou o número {}; \nseu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(num, 2 * num, 3 * num, num ** 0.5))
print('Você informou o número {}; \nseu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(num, 2 * num, 3 * num, pow(num, 0.5)))
