num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {num}.')
print(f'O número 9 apareceu {num.count(9)} vez(es).')
print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
print(f'O(s) valor(es) par(es) digitado(s) foi(ram) ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
