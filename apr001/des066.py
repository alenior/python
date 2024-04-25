num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Informe um número (insira 999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você inseriu um total de {cont} números, que somaram {soma}.')
