def index_difference(str1, str2):
    if str2 > str1:
        str1, str2 = str2, str1
    try:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                print('Het eerste verschil zit op index:', i)
                break
    except IndexError:
        print('Het eerst verschil zit op index:', i)


index_difference(input('Geef een string: '), input('Geef een string: '))
