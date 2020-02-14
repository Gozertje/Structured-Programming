import random
pins = ['A', 'B', 'C', 'D', 'E', 'F']

# Genereerd lijst met alle mogelijke antwoorden
ans_p = []
for x_1 in pins:
    for x_2 in pins:
        for x_3 in pins:
            for x_4 in pins:
                string = x_1 + x_2 + x_3 + x_4
                ans_p.append(string)


def generate_code():
    secrete_code = []
    for i in range(4):
        secrete_code.append(pins[random.randrange(6)])
    return secrete_code


def feedback(code, secrete_code):
    fb = {'Z': 0, 'W': 0}
    pinz = {'A': [0, 0, 0, 0], 'B': [0, 0, 0, 0], 'C': [0, 0, 0, 0], 'D': [0, 0, 0, 0], 'E': [0, 0, 0, 0], 'F': [0, 0, 0, 0]}
    for i in range(4):
        if code[i] == secrete_code[i]:
            fb['Z'] += 1
            if pinz[code[i]][i] == 1:
                fb['W'] -= 1
            pinz[code[i]][i] = 1
        else:
            for x in range(4):
                if code[i] == secrete_code[x] and pinz[code[i]][x] == 0:
                    fb['W'] += 1
                    pinz[code[i]][x] = 1
                    break
    return fb


def speler():
    secret_code = generate_code()
    tr = 0
    while tr < 10:
        gues = list(input('Doe een gok: ').upper())
        ant = feedback(gues, secret_code)
        print(ant)
        tr += 1
        if ant['Z'] == 4:
            print('Gelfeliciteerd je het gewonnen')

    print('Helaas verloren')


def mastermind():
    secret_code = list(input('Voer vier letters in A t/m F: ').upper())
    code = list(ans_p[random.randrange(1296)])
    print(code)
    print(feedback(code, secret_code))


que = input('Spelerm als \'Mastermind\' of \'Speler\': ').capitalize()
if que == 'Speler':
    speler()
else:
    mastermind()
