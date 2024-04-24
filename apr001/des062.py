primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termos = 10
termo = primeiro
while termos >= 1:
    termos -= 1
    print('{} '.format(termo), end='')
    termo += razao
    if termos == 0:
        termos = int(input('Deseja ver mais quantos termos? '))
        if termos == 0:
            print('Ok. Fim de PA.')
        else:
            continue
