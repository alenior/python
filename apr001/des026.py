frase = input('Informe uma frase: ')
print('Essa frase tem {} letras "a", a primeira aparece na posição {} e a última aparece na posição {}.'.format(frase.count('a'), frase.find('a'), frase.rfind('a')))
