valorDaCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do salário: '))
prazo = int(input('Informe em quantos anos deseja pagar a casa: '))
pmt = valorDaCasa / prazo / 12
if pmt <= salario * 0.3:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo não aprovado!')
