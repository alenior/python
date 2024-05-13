from random import randint


def sorteia(pri, ult, qtd):
    while qtd > 0:
        randint(pri, ult)
        qtd -= 1


pri = int(input('Informe o primeiro número da sequencia para sorteio: '))
ult = int(input('Informe o último número da sequencia para sorteio: '))
qtd = int(input('Informe a quantidade de números a ser sorteados: '))
while qtd > 0:
    sorteia(pri, ult, qtd)
