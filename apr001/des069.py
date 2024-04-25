cont = 1
tme18 = 0
hom = 0
mume20 = 0
cadastrar = 'S'
while cadastrar == 'S':
    idade = int(input(f'Informe a idade da {cont}ª pessoa: '))
    sexo = str(input(f'Informe o sexo da {cont}ª pessoa [M ou S]: ')).strip().upper()[0]
    if idade < 18:
        tme18 += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mume20 += 1
    cadastrar = str(input('Cadastrar outra pessoa? [S ou N] ')).strip().upper()[0]
    if cadastrar != 'S':
        break
    cont += 1
print(f'No total, foram cadastradas {cont} pessoas, sendo: {tme18} com menos de 18 anos, {hom} homem(ns) e {mume20} mulhere(s) com menos de 20 anos.')
