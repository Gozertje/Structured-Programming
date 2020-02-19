"""Kooi, B. (z.d.). YET ANOTHER MASTERMIND STRATEGY. Geraadpleegd van
https://canvas.hu.nl/courses/7474/assignments/68530"""
import random
from datetime import datetime
pins = ['A', 'B', 'C', 'D', 'E', 'F']

# Genereerd lijst met alle mogelijke antwoorden
ans_ps = []
for l_1 in pins:
    for l_2 in pins:
        for l_3 in pins:
            for l_4 in pins:
                string = l_1 + l_2 + l_3 + l_4
                ans_ps.append(string)


# Genereerd een random code
def generate_code(secret_code):
    for i in range(4):
        secret_code.append(pins[random.randrange(6)])
    return secret_code


# Geeft feedback op die ingevoerde code
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


# Input van de speler
def speler(tri, secret_code):
    while tri < 10:
        gues = list(input('Doe een gok: ').upper())
        ant = feedback(gues, secret_code)
        print(ant)
        tri += 1
        if ant['Z'] == 4:
            print('Gelfeliciteerd je het gewonnen')
    print('Helaas verloren')


# Berekent welke mogelijke feedback we kunnen krijgen
def one_step_a_head(counter):
    for i in ans_ps:
        structre = {'0.0': 0, '0.1': 0, '0.2': 0, '0.3': 0, '0.4': 0, '1.0': 0, '1.1': 0, '1.2': 0, '1.3': 0, '2.0': 0,
                    '2.1': 0, '2.2': 0, '3.0': 0, '4.0': 0}
        for x in ans_ps:
            ans = feedback(i, x)
            structre[str(ans['Z']) + '.' + str(ans['W'])] += 1
        counter[i] = structre
    return counter


# Berekent de 'expected case'
def worst_case(table, counter):
    structre = ['0.0', '0.1', '0.2', '0.3', '0.4', '1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.1', '2.2', '3.0', '4.0']
    for i in ans_ps:
        for x in structre:
            if table[i][x] != 0:
                if i in counter:
                    counter[i][1] += (table[i][x] ** 2) / len(ans_ps)
                else:
                    counter[i] = [i, (table[i][x] ** 2) / len(ans_ps)]
    return counter


# Checkt welke waarde het laagst is
def lowest_case(table):
    lowest = [0, 9999999]
    for i in ans_ps:
        if table[i][1] < lowest[1]:
            lowest = table[i]
    return lowest[0]


# Mogelijke antwoorden verwijderen
def brace(f_code, fb_1):
    ans_n = []
    for code in ans_ps:
        fb_2 = feedback(code, f_code)
        if fb_1 == fb_2:
            ans_n.append(code)
    return ans_n


# Input van de Computer
def mastermind(secret_code, tri):
    while tri < 10:
        global ans_ps
        if tri != 0:
            ans_ps = brace(code, fb)
            print(ans_ps)
            code = lowest_case(worst_case(one_step_a_head({}), {}))
        else:
            code = lowest_case(worst_case(one_step_a_head({}), {}))
        fb = (feedback(code, secret_code))
        print(fb, code)
        if fb['Z'] == 4:
            print("Gewonnen!")
            break
        tri += 1


que = input('Speler als \'Mastermind\' of \'Speler\': ').capitalize()
if que == 'Speler':
    speler(0, generate_code([]))
else:
    mastermind(list(input('Voer vier letters in A t/m F: ').upper()), 0)
