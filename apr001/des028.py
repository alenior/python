import random

num = random.randint(0, 5)
chute = int(input('Pensei em um número inteiro entre 0 e 5. Advinha qual foi? '))
if chute == num:
    print('CARALHO! ACERTOU DE PRIMEIRA, ARROMBADO! É {} MESMO!'.format(num))
elif chute > num:
    print('Errou! É menor!')
    while chute != num:
        chute = int(input('Tenta outro número: '))
        if chute == num:
            print('Você acertou! É {} mesmo!'.format(num))
        elif chute < num:
            print('Errou! É maior!')
        else:
            print('Errou! é menor!')
else:
    print('Errou! É maior!')
    while chute != num:
        chute = int(input('Tenta outro número: '))
        if chute == num:
            print('Você acertou! É {} mesmo!'.format(num))
        elif chute < num:
            print('Errou! É maior!')
        else:
            print('Errou! é menor!')
print('Fim de jogo!')
