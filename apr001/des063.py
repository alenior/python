qtd = int(input('Informe quantos números deseja exibir da seqüência de Fibonacci: '))
pen = 1
ult = 1
if qtd == 1:
    print('O 1º termo da sequência de Fibonacci é 1.')
if qtd == 2:
    print('Os 2 primeiros termos da sequência de Fibonacci são 1 1.')
print('Os {} primeiros termos da sequência de Fibonacci são 1 1 '.format(qtd), end='')
while qtd >= 3:
    fibo = ult + pen
    pen = ult
    ult = fibo
    qtd -= 1
    print('{} '.format(fibo), end='')
