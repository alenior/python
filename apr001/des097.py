def mensagem(msg):
    print('-' * (len(msg) + 2))
    print(f'{msg: ^{len(msg) + 2}}')
    print('-' * (len(msg) + 2))


msg = str(input('Qual a mensagem? '))
mensagem(msg)
