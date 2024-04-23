primeiro = int(input('Qual o primeiro termo da Progressão Aritmética? '))
razao = int(input('Qual a razão da Progressão Aritmética? '))
for c in range(primeiro, razao * 11, razao):
    print(c)
