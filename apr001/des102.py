def fatorial(num: int, exibir: bool = False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a se calcular o fatorial.
    :param exibir: (opcional) Mostrar ou não os cálculos.
    :return: O valor do fatorial de num.
    """

    fat = 1
    for a in range(num, 0, -1):
        if exibir:
            print(a, end='')
            if a > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= a
    return fat


print(fatorial(5, True))
help(fatorial)
