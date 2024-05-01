pares = []
impares = []
lista = [pares, impares]
for n in range(0, 7):
    num = int(input(f'Informe um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os números pares informados foram {sorted(pares)}.')
print(f'Os números ímpares informados foram {sorted(impares)}.')
