import random

temp = []
qtdn = 0

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
qtdj = int(input('Quantos jogos? '))
print(f'{f"Sorteando {qtdj} jogos:":^30}')
for j in range(0, qtdj):
    while qtdn < 6:
        num = random.randint(1, 60)
        if num in temp:
            continue
        else:
            temp.append(num)
            qtdn += 1
    qtdn = 0
    print(f'Jogo {j + 1}: {sorted(temp)}.')
    temp.clear()
print(f'{"BOA SORTE!":^30}')
