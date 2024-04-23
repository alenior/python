texto = str(input('Informe um texto para saber se é um palíndromo: '))
print(texto)
textoSemEspacos = texto.replace(' ', '')
print(textoSemEspacos)
textoTodoMinusculo = textoSemEspacos.lower()
print(textoTodoMinusculo)
textoInvertido = textoTodoMinusculo[::-1]
print(textoInvertido)
if textoTodoMinusculo == textoInvertido:
    print('Esse texto é um palíndromo!')
else:
    print('Esse texto não é um palíndromo!')
