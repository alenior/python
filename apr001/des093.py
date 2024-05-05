jogador = dict()
jogador['Nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = list()
total = 0
for p in range(0, partidas):
    gol = int(input(f' Quantos gols na partida {p}? '))
    gols.append(gol)
    total += gol
jogador['Gols'] = gols
jogador['Total'] = total
print('-=' * 30)
print(f'{jogador}')
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'  => Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {total} gols.')
