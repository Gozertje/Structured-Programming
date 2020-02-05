import random

while True:
    getal = input('Voer een getal in tussen de 0 en 10: ')
    r_num = random.randrange(10)
    if int(getal) == r_num:
        print('Juist')
        break
    else:
        print('Fout, het was', r_num)
