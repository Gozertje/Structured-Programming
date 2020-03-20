import psycopg2
import csv

# Maakt een conectie met de DB
table_names = []
c = psycopg2.connect("dbname=sp user=postgres password=Jopa2002jp")
cur = c.cursor()


# Slaat alle tabel namen op, om zo makkelijker de tabellen te kunnen exporteren naar een database
def write_table_names():
    with open('csv/#table_names.txt', 'w') as table_names_file:
        for name in table_names:
            table_names_file.write(name + '\n')
        table_names_file.close()


# Schrijft alle tabellen naar een csv bestand (wordt opgeslagen onder ../csv/)
def write_csv(f_name, content, field_name):
    global table_names
    table_names.append(f_name)
    with open('csv/' + f_name + '.csv', mode='w') as csv_file:
        fieldnames = field_name
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for var in content:
            csv_writer.writerow({field_name[0]: var})
        csv_file.close()


# Sorteert de producten op categorie en doelgroep
def sort_category():
    counter = {}
    cur.execute("""SELECT id, category, targetaudience FROM products""")
    query_results = cur.fetchall()
    for product in query_results:
        product = list(product)
        if product[1] is not None:
            if product[2] is None:
                product[2] = 'All'
            if (product[1] + product[2][1::2]) in counter:
                counter[(product[1] + product[2][1::2])] += [product[0]]
            else:
                counter[(product[1] + product[2][1::2])] = [product[0]]
    for category_name in counter:
        write_csv(category_name, counter[category_name], ['id'])


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid][0] == val:
            index = mid
        else:
            if val < lys[mid][0]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def sort_profiles():
    t = 0
    counter = {}
    cur.execute("""SELECT profid, os FROM sessions""")
    sessions = cur.fetchall()
    cur.execute("""SELECT profid, prodid FROM profiles_previously_viewed""")
    ppv = cur.fetchall()
    for session in sessions:
        product_i = BinarySearch(ppv, session[0])
        if session[1] in counter:
            counter[session[1]] += [ppv[product_i][1]]
        else:
            counter[session[1]] = [ppv[product_i][1]]
        ppv.remove(ppv[product_i])
        t += 1
        print(t)
    for os in counter:
        write_csv(os, counter[os], ['product'])


sort_category()
write_table_names()
sort_profiles()

