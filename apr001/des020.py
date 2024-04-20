import random

aluno1 = str(input('Informe o nome do 1º aluno: '))
aluno2 = str(input('Informe o nome do 2º aluno: '))
aluno3 = str(input('Informe o nome do 3º aluno: '))
aluno4 = str(input('Informe o nome do 4º aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A sequência de apresentação será {}.'.format(alunos))
