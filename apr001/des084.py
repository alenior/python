maior = list()
menor = list()
cont = 'S'
qtd = 0
while cont == 'S':
    nome = str(input('Informe o nome: '))
    peso = int(input('Informe o peso '))
    qtd += 1
    if qtd == 1:
        maior.append([nome, peso])
        menor.append([nome, peso])
    else:
        if peso == maior[0][1]:
            maior.append([nome, peso])
        elif peso > maior[0][1]:
            maior.pop()
            maior.append([nome, peso])
        elif peso == menor[0][1]:
            menor.append([nome, peso])
        elif peso < menor[0][1]:
            menor.pop()
            menor.append([nome, peso])
    cont = str(input('Continuar? [S] ou [N] ')).strip().upper()
print(f'A quantidade de pessoas informadas foi {qtd}.')
print(f'O maior peso informado foi {maior[0][1]}Kg. O peso de ', end='')
for n, p in maior:
    print(f'{n} ')
print(f'O menor peso informado foi {menor[0][1]}Kg. O peso de ', end='')
for n, p in menor:
    print(f'{n} ')
