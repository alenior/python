soma_das_idades = 0
quantidade = 0
mulheres_menos_de_20 = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
for p in range(1, 5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(p)))
    idade = int(input('Informe a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Informe o sexo (m ou f) da {}ª pessoa: '.format(p)))
    soma_das_idades += idade
    quantidade += 1
    if sexo == 'f' and idade < 20:
        mulheres_menos_de_20 += 1
    if sexo == 'm' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
print('A média de idade do grupo é {}, a quantidade de mulheres com menos de 20 anos é {} e o nome do homem mais velho é {}.'.format(soma_das_idades / quantidade), mulheres_menos_de_20, nome_homem_mais_velho)
