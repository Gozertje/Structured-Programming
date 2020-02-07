text = list(input('Geef een tekst: '))
rot = int(input('Geef een rotatie: '))

for lt in range(len(text)):
    text[lt] = chr(ord(text[lt]) + rot)
print('Ceasarcode:', ''.join(text))
