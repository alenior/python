soma = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        soma += x
print('A soma dos números ímpares entre 1 e 500 que são múltiplos de 3 é: {}.'.format(soma))
