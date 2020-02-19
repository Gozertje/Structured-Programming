"""Kooi, B. (z.d.). YET ANOTHER MASTERMIND STRATEGY. Geraadpleegd van
https://canvas.hu.nl/courses/7474/assignments/68530"""
import random
pins = ['A', 'B', 'C', 'D', 'E', 'F']

# Genereerd lijst met alle mogelijke antwoorden
ans_ps = []
for lt_1 in pins:
    for lt_2 in pins:
        for lt_3 in pins:
            for lt_4 in pins:
                string = lt_1 + lt_2 + lt_3 + lt_4
                ans_ps.append(string)


# Genereerd een random code
def generate_code(secret_code):
    for letter in range(4):
        secret_code.append(pins[random.randrange(6)])
    return secret_code


# Geeft feedback op die ingevoerde code
def feedback(code, secrete_code):
    fb = {'Z': 0, 'W': 0}
    pinz = {'A': [0, 0, 0, 0], 'B': [0, 0, 0, 0], 'C': [0, 0, 0, 0], 'D': [0, 0, 0, 0], 'E': [0, 0, 0, 0],
            'F': [0, 0, 0, 0]}
    for index in range(4):
        if code[index] == secrete_code[index]:
            fb['Z'] += 1
            if pinz[code[index]][index] == 1:
                fb['W'] -= 1
            pinz[code[index]][index] = 1
        else:
            for index_s in range(4):
                if code[index] == secrete_code[index_s] and pinz[code[index]][index_s] == 0:
                    fb['W'] += 1
                    pinz[code[index]][index_s] = 1
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
    for code_1 in ans_ps:
        structre = {'0.0': 0, '0.1': 0, '0.2': 0, '0.3': 0, '0.4': 0, '1.0': 0, '1.1': 0, '1.2': 0, '1.3': 0, '2.0': 0,
                    '2.1': 0, '2.2': 0, '3.0': 0, '4.0': 0}
        for code_2 in ans_ps:
            ans = feedback(code_1, code_2)
            structre[str(ans['Z']) + '.' + str(ans['W'])] += 1
        counter[code_1] = structre
    return counter


# Berekent de 'expected case'
def worst_case(table, counter):
    structre = ['0.0', '0.1', '0.2', '0.3', '0.4', '1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.1', '2.2', '3.0', '4.0']
    for code_1 in ans_ps:
        for code_2 in structre:
            if table[code_1][code_2] != 0:
                if code_1 in counter:
                    counter[code_1][1] += (table[code_1][code_2] ** 2) / len(ans_ps)
                else:
                    counter[code_1] = [code_1, (table[code_1][code_2] ** 2) / len(ans_ps)]
    return counter


# Checkt welke waarde het laagst is
def lowest_case(table):
    lowest = [0, 9999999]
    for code in ans_ps:
        if table[code][1] < lowest[1]:
            lowest = table[code]
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
            code = lowest_case(worst_case(one_step_a_head({}), {}))
        else:
            code = lowest_case(worst_case(one_step_a_head({}), {}))
        fb = (feedback(code, secret_code))
        print(code, 'geeft:', (str(fb['Z']) + ',' + str(fb['W'])))
        if fb['Z'] == 4:
            print("Gewonnen!")
            break
        tri += 1


def put_in():
    que = input('Spelen als \'Mastermind\' of \'Speler\': ').capitalize()
    if que == 'Speler':
        speler(0, generate_code([]))
    elif que == 'Mastermind':
        mastermind(list(input('Voer vier letters in A t/m F: ').upper()), 0)
    else:
        put_in()


put_in()
