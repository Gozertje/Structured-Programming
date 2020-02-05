def count(lst):
    n_lst = {}
    for num in lst:
        if num in n_lst:
            n_lst[num] += 1
        else:
            n_lst[num] = 1
    return n_lst


def b_dif(lst):
    dif = 0
    for num in range(len(lst) - 1):
        if abs(lst[num] - lst[num + 1]) > dif:
            dif = abs(lst[num] - lst[num + 1])
    print(dif)


def one_and_zero(lst):
    lst = count(lst)
    if lst[1] > lst[0] and lst[0] <= 12:
        print('Lijst voldoet aan eisen')
    else:
        print('Lijst voldoet niet aan eisen')


lijst = [2, 5, 8, 5, 6, 8, 3, 2, 1, 1, 1, 7, 5, 4, 8, 9, 2, 10, 4, 6, 2, 8, 3, 6, 4, 5]
lijst_0 = [0, 0, 0, 1, 1, 1, 1]
count(lijst)
b_dif(lijst)
one_and_zero(lijst_0)
