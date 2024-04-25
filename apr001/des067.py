num = 0
cont = 0
while num >= 0:
    num = int(input('Informe um números para ser exibida sua tabuada: '))
    if num < 0:
        break
    while cont <= 10:
        print(f'{num:2} X {cont:2} = {(num * cont):2}')
        cont += 1
    cont = 0
print(f'\nFim de programa!')
