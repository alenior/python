aluno = {}
nome = str(input('Nome: '))
aluno['Nome'] = nome
media = float(input(f'Média de {nome}: '))
aluno['Média'] = media
print(f'Nome é igual a {aluno["Nome"]}.')
print(f'Média é igual a {aluno["Média"]}.')
if media >= 7:
    print('Situação é igual a Aprovado.')
else:
    print('Situação é igual a Reprovado.')
