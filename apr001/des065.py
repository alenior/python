soma = 0
qtd = 0
maior = menor = 0
perg = str(input('Informar valor? [S / N] ')).strip().upper()
if perg != 'S':
    print('Ok. Encerrando programa.')
else:
    while perg == 'S':
        num = int(input('Qual o valor? '))
        soma += num
        qtd += 1
        if qtd == 1:
            maior = num
            menor = num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        perg = str(input('Informar valor? ')).strip().upper()
    print('Você informou {} valor(es), a média deles é {}, o maior é o {} e o menor é o {}.'
          .format(qtd, soma / qtd, maior, menor))
