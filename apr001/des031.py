distancia = float(input('Qual a distância, em Km, da viagem? '))
if distancia < 200:
    print('O valor da passagem é R$ {}.'.format(distancia * 0.50))
else:
    print('O valor da passagem é R$ {}.'.format(distancia * 0.45))
