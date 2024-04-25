import random

res = ''
vit = ''
cont = 0
while vit != 'Computador':
    comp = random.randint(0, 10)
    jog = int(input('Diga um valor (0 a 9): '))
    poi = str(input('Par ou ímpar [P/I]? ')).strip().upper()
    if (comp + jog) % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'
    if (poi == 'P' and res == 'PAR') or (poi == 'I' and res == 'ÍMPAR'):
        vit = 'Você'
    else:
        vit = 'Computador'
    cont += 1
    print(f'Você jogou {jog} e o computador jogou {comp}. Deu {res}. {vit} venceu!\n')
print(f'Você jogou {cont} veze(s) antes de perder.')
