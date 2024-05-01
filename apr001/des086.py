lista = [[], [], []]
qtd = i = c = 0
for q in range(0, 9):
    num = int(input(f'Informe um número para [{i}, {c}]: '))
    lista.insert(num, [i][c])
    if c < 2:
        c += 1
    elif c == 2:
        c = 0
        i += 1
    qtd += 1
print(f'{lista[[0][0]]} {lista[[0][1]]} {lista[[0][2]]}\n{lista[[1][0]]} {lista[[1][1]]} {lista[[1][2]]}\n{lista[[2][0]]} {lista[[2][1]]} {lista[[2][2]]}')
