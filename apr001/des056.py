somaIdade = 0
mediaIdade = 0
maioIdadeHomem = 0
nomeHomemMaisVelho = ''
mulherMenosDe20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maioIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Mm' and idade > maioIdadeHomem:
        maioIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherMenosDe20 += 1
mediaIdade = somaIdade / 4

print('A média de idade do grupo é {:.1f} anos.'.format(mediaIdade))
print('O homem mais velho tem {:.0f} anos e se chama {}.'.format(maioIdadeHomem, nomeHomemMaisVelho))
print('O total de mulheres com menos de 20 anos é {}.'.format(mulherMenosDe20))
