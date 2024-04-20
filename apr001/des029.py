vel = float(input('Qual a velocidade do carro? '))
if vel < 80:
    print('Continue dirigindo com segurança. Boa viagem!')
else:
    print('Eita! Vai parir gêmeos normal? Que pressa é essa?! Você foi multado em R$ {:.2f}. Bem feito!'.format((vel - 80) * 7))
