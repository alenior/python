import datetime

maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if (datetime.date.today().year - nascimento) < 18:
        menores += 1
    else:
        maiores += 1
print('Dos informados, {} é/são maior(es) e {} é/são menor(es).'.format(maiores, menores))
