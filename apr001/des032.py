import datetime

ano = int(input('Informe um ano para saber se ele é, foi ou será bisexto (informe 0 para analisar o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if int(ano) % 4 != 0:
    print('O ano {} não é/foi/será bissexto.'.format(ano))
elif str(ano)[-2:] == '00' and int(ano) % 400 != 0:
    print('O ano {} não é/foi/será bissexto.'.format(ano))
else:
    print('O ano {} é/foi/será bissexto!'.format(ano))
