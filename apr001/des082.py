lista = []
pares = []
impares = []
num = 0
while num != -1:
    num = int(input(f'Informe um número(-1 finaliza): '))
    if num > -1:
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
print(f'Os números digitados foram: {lista}.')
print(f'O(s) número(s) par(es) digitado(s) é(são): {pares}.')
print(f'O(s) número(s) impa(es) digitado(s) é(são): {impares}.')
