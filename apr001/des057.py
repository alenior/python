sexo = str(input('Digite seu sexo [M ou F]: ')).strip().upper()
while sexo not in 'MF':
    print('Opção inválida!')
    sexo = str(input('Digite seu sexo [M ou F]: ')).strip().upper()
if sexo in 'M':
    print('Seu sexo é Masculino!')
else:
    print('Seu sexo é Feminino!')
