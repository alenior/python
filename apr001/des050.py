somaPares = 0
for x in range(1, 7):
    num = int(input('Digite um número; '))
    if num % 2 == 0:
        somaPares += num
print('\nA soma dos números pares informados é {}.'.format(somaPares))
