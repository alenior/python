catetoO = float(input('Informe o valor do cateto oposto: '))
catetoA = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = pow((catetoO**2) + (catetoA**2), 0.5)
print('Um triângulo com valores de catetos {} e {} tem hipotenusa de valor {}.'.format(catetoO, catetoA, hipotenusa))
