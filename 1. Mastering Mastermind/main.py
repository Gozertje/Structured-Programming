"""Kooi, B. (z.d.). YET ANOTHER MASTERMIND STRATEGY. Geraadpleegd van
https://canvas.hu.nl/courses/7474/assignments/68530"""
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


def one_step_a_head():
    counter = {}
    for i in ans_p:
        structre = {'0.0': 0, '0.1': 0, '0.2': 0, '0.3': 0, '0.4': 0, '1.0': 0, '1.1': 0, '1.2': 0, '1.3': 0, '2.0': 0,
                    '2.1': 0, '2.2': 0, '3.0': 0, '4.0': 0}
        for x in ans_p:
            ans = feedback(i, x)
            structre[str(ans['Z']) + '.' + str(ans['W'])] += 1
        counter[i] = structre
    return counter


def worst_case(table):
    counter = {}
    structre = ['0.0', '0.1', '0.2', '0.3', '0.4', '1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.1', '2.2', '3.0', '4.0']
    for i in ans_p:
        for x in structre:
            if table[i][x] != 0:
                if i in counter:
                    counter[i][1] += (table[i][x] ** 2) / 1296
                else:
                    counter[i] = [i, (table[i][x] ** 2) / 1296]
    return counter


def algo(table):
    lowest = [0, 9999999]
    for i in ans_p:
        if table[i][1] < lowest[1]:
            lowest = table[i]
    return lowest[0]


def brace(f_code, fb_1):
    ans_n = []
    for code in ans_p:
        fb_2 = feedback(code, f_code)
        if fb_1 == fb_2:
            ans_n.append(code)
    return ans_n


def mastermind():
    tr = 0
    secret_code = list(input('Voer vier letters in A t/m F: ').upper())
    while tr < 10:
        global ans_p
        if tr != 0:
            ans_p = brace(code, fb)
            print(ans_p)
            code = algo(worst_case(one_step_a_head()))
        else:
            code = algo(worst_case(one_step_a_head()))
        fb = (feedback(code, secret_code))
        print(fb, code)
        if fb['Z'] == 4:
            print("Gewonnen!")
            break
        tr += 1
    print('Verloren')


que = input('Spelerm als \'Mastermind\' of \'Speler\': ').capitalize()
if que == 'Speler':
    speler()
else:
    mastermind()
