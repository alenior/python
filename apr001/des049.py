num = int(input('Tabuada de qual número? '))
print('\n')
for x in range(1, 11):
    print('{:2}  X {:2} = {:2}'.format(x, num, x * num))
