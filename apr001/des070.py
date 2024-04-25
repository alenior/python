continuar = 'S'
tgasto = 0
tmais1000 = 0
maisBarato = ''
qtd = 1
while continuar == 'S':
    nome = str(print(f'Nome do {qtd}º produto: ')).strip().upper()
    preco = float(input(f'Preço do {qtd}º produto: '))
    if qtd == 1:
