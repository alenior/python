def area(c, l):
    print(f'A área do terreno retangular é {l * c:.2f} m².')


print(f'{"CONTROLE DE TERRENOS":-^30}')
l = float(input('Informe a largura do terreno retangular (m): '))
c = float(input('Informe o comprimento do terreno retangular (m): '))
area(c, l)
