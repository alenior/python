import cv2

valorDaCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do salário: '))
prazo = int(input('Informe em quantos anos deseja pagar a casa: '))
pmt = valorDaCasa / prazo / 12
if pmt <= salario * 0.3:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo não aprovado!')

imagem = cv2.imread("print (, end='').png")
cv2.imshow("unirPrints", imagem)

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d" % (imagem.shape[2]))

cv2.waitKey(0)
