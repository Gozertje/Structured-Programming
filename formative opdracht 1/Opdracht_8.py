def compressie(lst):
    lst = lst.split('\n')
    x = ''
    for i in lst:
        if i != '':
            i = i.lstrip()
            x += i + '\n'
    with open('n_txt.txt', 'w') as n_txt_file:
        n_txt_file.write(x)
        n_txt_file.close()


with open('txt.txt', 'r') as txt_file:
    data = txt_file.read()
    compressie(data)
    txt_file.close()
