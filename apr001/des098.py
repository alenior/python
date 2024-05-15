from time import sleep


def contador(ini, fim, pas):
    if ini < fim:
        while ini <= fim:
            print(f'{ini} ', end='')
            sleep(1)
            ini += pas
    elif ini > fim:
        while ini >= fim:
            print(f'{ini} ', end='')
            sleep(1)
            ini -= pas
    else:
        print(f'{ini}.')
        sleep(1)


ini = int(input('Qual o número inicial? '))
fim = int(input('Qual o número final? '))
pas = int(input('Qual o passo? '))
contador(ini, fim, pas)
