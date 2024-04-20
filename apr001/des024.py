cidade = input('Informe o nome de uma cidade: ')
dividido = cidade.split()
if 'Santo' in dividido[0]:
    print('A cidade informada tem "Santo" no começo do nome.')
else:
    print('A cidade informada não tem "Santo" no começo do nome.')
