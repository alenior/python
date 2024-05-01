matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = soma3 = maior2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if matriz[l][1] > maior2:
            maior2 = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares é {somaPar}.')
print(f'A soma dos números da 3ª coluna é {soma3}.')
print(f'O maior número da 2ª coluna é o {maior2}.')
