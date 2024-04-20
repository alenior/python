reta1 = float(input('Informe o tamanho da 1ª reta: '))
reta2 = float(input('Informe o tamanho da 2ª reta: '))
reta3 = float(input('Informe o tamanho da 3ª reta: '))
soma = reta1 + reta2 + reta3
maior = max(reta1, reta2, reta3)
demais = soma - maior
if maior < demais:
    print('É possível um triângulo de lados {}, {} e {}.'.format(reta1, reta2, reta3))
else:
    print('Não é possível um triângulo de lados {}, {} e {}.'.format(reta1, reta2, reta3))
