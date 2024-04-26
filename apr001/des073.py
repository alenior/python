classificacao = ('Corínthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
                 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória',
                 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
col = 0
while col <= 4:
    if col == 0:
        print(f'Seguem os 5 primeiros colocados: ')
    print(f'{col + 1}º: {classificacao[col]}')
    col += 1
print('')
col = 16
while col <= 19:
    if col == 16:
        print(f'Seguem os 4 últimos colocados: ')
    print(f'{col + 1}º: {classificacao[col]} ')
    col += 1
print('')
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print('')
print(f'A Chapecoense está na {classificacao.index("Chapecoense") + 1}ª posição.')
