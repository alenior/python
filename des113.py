def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


ni = leiaInt('Digite um inteiro: ')
nf = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {ni} e o valor real digitado foi {nf}.')
