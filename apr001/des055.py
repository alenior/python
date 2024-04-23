peso = 0
maior = peso
menor = peso
for p in range(1, 6):
    peso = float(input('informe o peso da {}ª pessoa: '.format(p)))
    maior = max(maior, peso)
    menor = min(menor, peso)
print('\nDos 5 pesos informados, o maior é {} e o menor é {}.'.format(maior, menor))
