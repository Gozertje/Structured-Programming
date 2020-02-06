def bereken(ch, n):
    t = 0
    if t != n:
        index = ch[t]
        ch.pop(t)
        ch.append(index)
        t += 1
    return ch


def cyclisch(ch, n):
    if n < 0:
        ch = ch[::-1]
        bereken(ch, abs(n)).reverse()
    else:
        bereken(ch, n)
    print(''.join(ch))


cyclisch(list('1011100'), -4)
