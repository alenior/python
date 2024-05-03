alunos = []
pos = 0
indicea = 0
continuar = 'S'
print('Insira as informações para gerar o boletim da turma:\n')
while continuar == 'S':
    temp = []
    nome = str(input('Nome: '))
    temp.insert(pos, nome)
    n1 = int(input('Nota 1: '))
    temp.insert(pos + 1, n1)
    n2 = int(input('Nota 2: '))
    temp.insert(pos + 2, n2)
    alunos.insert(indicea, temp[:])
    pos = 0
    indicea += 1
    temp.clear()
    continuar = str(input('Continuar? [S/N] ')).strip().upper()
print('-=' * 30)
print(f'{f"Nº": <3} {f"Nome": <10} {f"Média": <10}')
for a in range(0, len(alunos)):
    print(f'{a: <3} {alunos[a][0]: <10} {((alunos[a][1] + alunos[a][2]) / 2): <10.2f}')
num = 0
while num != -1:
    num = int(input('Mostrar notas de qual aluno? (-1 finaliza) '))
    print(f'Notas de {alunos[num][0]} são {alunos[num][1]} e {alunos[num][2]}.')
print('\nFim de detalhamento.')
