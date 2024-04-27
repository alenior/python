lista = []
continuar = 'S'
while continuar == 'S':
    num = int(input(f'Informe um número: '))
    if num not in lista:
        lista.append(num)
        print(f'Número adicionado com sucesso!')
        continuar = str(input(f'Continuar? ')).strip().upper()[0]
    else:
        print(f'Número já está na lista. Não será adicionado...')
        continuar = str(input(f'Continuar? ')).strip().upper()[0]
print(f'-=' * 15)
print(f'Você digitou os números {sorted(lista)}.')
