from datetime import datetime

pessoas = dict()
pessoas['Nome'] = str(input('Nome: '))
pessoas['Ano'] = int(input('Ano de nascimento: '))
pessoas['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoas['Ctps'] != 0:
    pessoas['Contratação'] = int(input('Ano da contratação: '))
    pessoas['Aposentadoria'] = pessoas['Contratação'] - pessoas['Ano'] + 35
    pessoas['Salário'] = float(input('Salário: R$ '))
print('-=' * 30)
for k, v in pessoas.items():
    print(f' - {k} tem o valor {v}.')

'''print(f' - O nome é {pessoas["Nome"]}.')
print(f' - A idade é {datetime.now().year - pessoas["Ano"]}.')
print(f' - A CTPS tem o número {pessoas["Ctps"]}.')
if pessoas['Ctps'] != 0:
    print(f' - O ano da contratação foi {pessoas["Contratação"]}.')
    print(f' - O valor do salário é R$ {pessoas["Salário"]:.2f}.')
    print(f' - A aposentadoria será aos {pessoas["Contratação"] - pessoas["Ano"] + 35} anos.')'''
