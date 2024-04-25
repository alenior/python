continuar = 'S'
tgasto = 0
tmais1000 = 0
maisBarato = ''
precoMaisBarato = 0
qtd = 1
while continuar == 'S':
    nome = str(input(f'Nome do {qtd}º produto: ')).strip().upper()
    preco = float(input(f'Preço do {qtd}º produto: R$ '))
    if qtd == 1:
        maisBarato = nome
        precoMaisBarato = preco
    if preco < precoMaisBarato:
        maisBarato = nome
        precoMaisBarato = preco
    if preco > 1000:
        tmais1000 += 1
    tgasto += preco
    continuar = str(input(f'Continuar? [S ou N] ')).strip().upper()
    if continuar == 'S':
        qtd += 1
print(f'O total gasto na compra foi {tgasto:.2f}, {tmais1000} produtos custaram mais de R$ 1000,00 e o produto mais '
      f'barato foi o {maisBarato}, que custou R$ {precoMaisBarato:.2f}.')
