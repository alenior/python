num = int(input('Informe um número: '))
ant = num - 1
suc = num + 1
print('O número citado foi o {}, seu antecessor é o {} e o sucessor é o {}.'.format(num, ant, suc))
print('O número citado foi o {}, seu antecessor é o {} e o sucessor é o {}.'.format(num, (num - 1), (num + 1))) # Menos variáveis, menos espaço necessário na memória.
