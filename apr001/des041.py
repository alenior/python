import datetime

anoNascimento = int(input('Informe seu ano de nascimento: '))
idade = datetime.date.today().year - anoNascimento
if idade <= 9:
    print('Você é da categoria MIRIM!')
elif 9 < idade <= 14:
    print('Você é da categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Você é da categoria JÚNIOR!')
elif 19 < idade <= 20:
    print('Você é da categoria SÊNIOR!')
else:
    print('Você é da categoria MASTER!')
