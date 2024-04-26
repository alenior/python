import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)
num5 = random.randint(0, 9)
tupla = (num1, num2, num3, num4, num5)
print(tupla)
print(f'Maior: {max(tupla)}.')
print(f'Menor: {min(tupla)}.')
