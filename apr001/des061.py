primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termos = 10
termo = primeiro
while termos >= 1:
    termo = termo + razao
    termos -= 1
    print('{} '.format(termo), end='')
