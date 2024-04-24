qtd = 0
soma = 0
num = int(input('Informe um número: '))
while num != 999:
    qtd += 1
    soma += num
    num = int(input('Informe outro número: '))
print('Você informou {} números que somam {}.'.format(qtd, soma))
