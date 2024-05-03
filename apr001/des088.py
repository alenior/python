import random
import time

temp = []
qtdn = 0
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
qtdj = int(input('Quantos jogos? '))
print(f'{f"Sorteando {qtdj} jogo(s):":^30}')
time.sleep(1)
for j in range(0, qtdj):
    while qtdn < 6:
        num = random.randint(1, 60)
        if num in temp:
            continue
        else:
            temp.append(num)
            qtdn += 1
    qtdn = 0
    print(f'\nJogo {j + 1}: {sorted(temp)}.')
    temp.clear()
print(f'\n{"BOA SORTE!":^30}')
