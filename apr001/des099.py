def maior(* num):
    numeros = []
    qtd = 0
    bigger = 0
    continuar = 'S'
    while continuar == 'S':
        num = int(input('Informe um número para adicionar à análise do MAIOR: '))
        if qtd == 0:
            bigger = num
        else:
            if num > bigger:
                bigger = num
        qtd += 1
        numeros.append(num)
        continuar = str(input('Adicionar número? ')).strip().upper()
    print(f'Os números informados foram {numeros}.')
    print(f'O maior deles é o {bigger}.')


maior()
