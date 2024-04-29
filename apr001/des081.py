lista = []
qtd = 0
cinco = False
while True:
    num = int(input(f'Informe um número (-1 finaliza): '))
    if num == 5:
        cinco = True
    if num == -1:
        break
    lista.append(num)
    qtd += 1
print(f'Foram digitados {qtd} números.')
listaDecrescente = sorted(lista, reverse=True)
print(f'A lista em ordem decrescente é {listaDecrescente}.')
if cinco == True:
    print(f'O número 5 está na lista!')
