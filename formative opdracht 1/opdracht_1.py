# For loops
length = int(input("Hoe groot?: "))

for at in range(1, length + 1):
    print(at * '*')
for at in range(1, length):
    print((length - at) * '*')


print(' ')


# While loops
at = 0
while at != length:
    at += 1
    print(at * '*')
while at != 1:
    at -= 1
    print(at * '*')


print('')


# Reversed for loops
for at in range(1, length + 1):
    print((length - at) * ' ' + at * '*')
for at in range(1, length):
    print(at * ' ' + (length - at) * '*')


print('')


# Reversed while loops
at = 0
while at != length:
    at += 1
    print((length - at) * ' ' + at * '*')
while at != 1:
    at -= 1
    print((length - at) * ' ' + at * '*')
