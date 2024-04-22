nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('APROVADO!')
elif 5 <= media < 7:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')
