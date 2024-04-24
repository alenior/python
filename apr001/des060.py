numI = int(input('Informe um número para determinar seu fatorial: '))
fat = numI
numA = numI
while numA > 1:
    fat = fat * (numA - 1)
    numA -= 1
print('O fatorial de {} é {}.'.format(numI, fat))
