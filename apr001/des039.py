import datetime

nascimento = int(input('Informe o ano de nascimento: '))
if (datetime.date.today().year - nascimento) < 18:
    print('Falta(m) {} ano(s) para você se alistar.'.format(18 - (datetime.date.today().year - nascimento)))
elif (datetime.date.today().year - nascimento) > 18:
    print('Faz {} ano(s) que você deveria ter se alistado.'.format((datetime.date.today().year - nascimento) - 18))
else:
    print('Você deve se alistar esse ano!')
