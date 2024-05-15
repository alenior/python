from random import randint


def sorteia(pri, ult, qtd):
    sorteados = []
    while qtd > 0:
        sorteados.append(randint(pri, ult))
        qtd -= 1
    print(f'{sorteados}')


def somaPar():



pri = int(input('Informe o primeiro número da sequencia para sorteio: '))
ult = int(input('Informe o último número da sequencia para sorteio: '))
qtd = int(input('Informe a quantidade de números a ser sorteados: '))
sorteia(pri, ult, qtd)
