import random
colors = ['geel', 'wit', 'zwart', 'groen', 'rood', 'blauw']


def create_code(code):
    for i in range(4):
        code.append(colors[random.randrange(6)])
    return code


def check_code(code, ant, i, secret_code):
    for x in range(4):
        if code[i] == secret_code[x]:
            ant += code[i] + ' : W '
            return ant
    ant += code[i] + ' :  '
    return ant


def speler():
    print('Te gebruiken kleuren: geel, wit, zwart, groen, rood, blauw ')
    secret_code = create_code([])
    tr = 0
    while tr < 10:
        ant = ''
        code = input('Voer vier kleuren in: ').split(' ')
        if code == secret_code:
            print('Gelfeliciteerd!, je hebt gewonnen')
            break
        else:
            for i in range(4):
                if code[i] == secret_code[i]:
                    ant += code[i] + ' : Z '
                else:
                    ant = check_code(code, ant, i, secret_code)
        tr += 1
        print(ant)


def mastermind():
    print('#')


que = input('Spelen als \'Mastermind\' of als \'Speler\': ')
if que.capitalize() == 'Speler':
    speler()
else:
    mastermind()
