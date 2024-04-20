salario = float(input('Informe seu salário: '))
if salario > 1250:
    print('O seu aumento será de R$ {}.'.format(salario * .1))
else:
    print('O seu aumento será de R$ {}.'.format(salario * .15))
