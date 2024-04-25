contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito' 'dezenove', 'vinte'
            )
num = int(input('Informe um número entre 0 e 20 para exibir sua denominação por extenso: '))
print(f'\nO número {num} por extenso é {contagem[num]}.')
