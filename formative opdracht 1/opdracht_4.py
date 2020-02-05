woord = input('Voer een string in: ')

if woord == woord[::-1]:
    print(woord, "is een palindroom")
else:
    print(woord, 'is geen palindroom')
