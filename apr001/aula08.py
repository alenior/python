import math  # from math import sqrt, floor

num = float(input('Informe um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}.'.format(num, raiz))
print('A raiz quadrada de {} é {:.2f}.'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é {:.2f}.'.format(num, math.floor(raiz)))
