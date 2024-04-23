"""
number = int(input('Informe um número pra saber se ele é primo: '))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo.')
            break
        else:
            print(number, 'é primo.')
elif number == 0:
    print(number, 'é zero!')
elif number == 1:
    print(number, 'é um!')
else:
    print(number, 'é negativo!')
"""

num = int(input('Informe um número para saber se ele é primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E, por isso, ele é primo!')
else:
    print('E, por isso, ele não é primo!')
