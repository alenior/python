num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
if num1 > num2:
    print('O número {} é o maior.'.format(num1))
elif num2 > num1:
    print('O número {} é o maior.'.format(num2))
else:
    print('Os dois números são iguais!')
