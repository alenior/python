import random

computador = random.randint(0, 10)
chute = int(input('Pensei num número entre 0 e 10. Advinha qual foi? '))
chutes = 1
while chute != computador:
    if chute < computador:
        chute = int(input('Errou! É maior! Outro chute? '))
        chutes += 1
    else:
        chute = int(input('Errou! É menor! Outro chute? '))
print('Acertou! Pensei no {} mesmo!'.format(chute))
print('Você chutou {} vez(es) para acertar!'.format(chutes))
