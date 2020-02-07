def fibonaci(fn, n):
    if n != 0:
        x = fn[0] + fn[1]
        fn[0], fn[1] = fn[1], x
        n -= 1
        fibonaci(fn, n)
    else:
        return print(fn[0])


f = int(input('Voer een getal in: '))
fibonaci([0, 1], f)
