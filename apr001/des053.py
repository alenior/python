"""texto = str(input('Informe um texto para saber se é um palíndromo: '))
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
    print('Esse texto não é um palíndromo!')"""

texto = str(input('Informe um texto para verificar se é um palíndromo: ')).strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
