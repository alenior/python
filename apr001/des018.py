import math

angulo = float(input('Informe um ângulo qualquer: '))
anguloRadianos = math.radians(angulo)
print('O ângulo {}º tem, respectivamente, os seguintes valores de seno, cosseno e tangente: {:.5f}, {:.5f} e {:.5f}.'.format(angulo, math.sin(anguloRadianos), math.cos(anguloRadianos), math.tan(anguloRadianos)))
