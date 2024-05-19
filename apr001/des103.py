def ficha(nome: str = '<desconhecido>', gols: int = 0):
    """
    -> Função que informa o nome do jogador e sua quantidade de gols.
    :param nome: Nome do jogador.
    :param gols: Quantidade de gols do jogador.
    :return: Informação com os parâmetros informados.
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Informe o nome do jogador: '))
g = str(input('Informe o número de gols do jogador: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

help(ficha)
