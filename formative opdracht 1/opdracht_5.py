lijst = [2, 5, 8, 5, 6, 8, 3, 2, 1, 1, 1, 7, 5, 4, 8, 9, 2, 10, 4, 6, 2, 8, 3, 6, 4, 5]


def sort(lst):
    i = 0
    for num in range(len(lst) - 1):
        if lst[num] > lst[num + 1]:
            lst[num], lst[num + 1] = lst[num + 1], lst[num]
            i = 1
    if i == 0:
        print(lst)
    else:
        sort(lst)


sort(lijst)
