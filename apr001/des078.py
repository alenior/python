qtd = 0
lista = []
while qtd < 5:
    num = int(input(f'Informe o {qtd + 1} número: '))
    lista.insert(qtd, num)
    qtd += 1
print(f'O maior número da lista é o {max(lista)} (posição {lista.index(max(lista)) + 1}) e o menor é o '
      f'{min(lista)} (posição {lista.index(min(lista)) + 1}.')
