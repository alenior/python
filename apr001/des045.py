import random
import time
import cv2

usuario = int(input('Papel (0), tesoura (1) ou pedra (2)? '))
maquina = random.randint(0, 2)

if usuario == 0 and maquina == 0:
    print('\nUsuário escolheu Papel. A máquina escolheu...')
    time.sleep(2)
    print('Papel!')
    time.sleep(1)
    print('\nEmpate! Ambos escolheram papel!')
elif usuario == 0 and maquina == 1:
    print('\nUsuário escolheu papel. A máquina escolheu...')
    time.sleep(2)
    print('Tesoura!')
    time.sleep(1)
    print('\nMáquina ganha! A tesoura da máquina corta o papel do usuário!')
elif usuario == 0 and maquina == 2:
    print('\nUsuário escolheu papel. A máquina escolheu...')
    time.sleep(2)
    print('Pedra!')
    time.sleep(1)
    print('\nUsuário ganha! O papel do usuário envolve a pedra da máquina!')
elif usuario == 1 and maquina == 0:
    print('\nUsuário escolheu tesoura. A máquina escolheu...')
    time.sleep(2)
    print('Papel!')
    time.sleep(1)
    print('\nUsuário ganha! A tesoura do usuário corta o papel da máquina!')
elif usuario == 1 and maquina == 1:
    print('\nUsuário escolheu tesoura. A máquina escolheu...')
    time.sleep(2)
    print('Tesoura!')
    time.sleep(1)
    print('\nEmpate! Ambos escolheram tesoura!')
elif usuario == 1 and maquina == 2:
    print('\nUsuário escolheu Tesoura. A máquina escolheu...')
    time.sleep(2)
    print('Pedra!')
    print('\nMáquina ganha! A pedra da máquina quebra a tesousa do usuário!')
elif usuario == 2 and maquina == 0:
    print('\nUsuário escolheu Pedra. a máquina escolheu...')
    time.sleep(2)
    print('Papel!')
    print('\nMáquina ganha! O papel da máquina envolve a pedra do usuário!')
elif usuario == 2 and maquina == 1:
    print('\nUsuário escolheu Pedra. A máquina escolheu...')
    time.sleep(2)
    print('Tesoura!')
    print('\nUsuário ganha! A Pedra do usuário quebra a tesoura da máquina!')
else:
    print('\nUsuário escolheu Pedra. A máquina escolheu...')
    time.sleep(2)
    print('Pedra!')
    time.sleep(1)
    print('\nEmpate! Ambos escolheram pedra!')

imagem = cv2.imread("usoDeLista.png")
cv2.imshow("Uso de Lista", imagem)

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d" % (imagem.shape[2]))

cv2.waitKey(0)
