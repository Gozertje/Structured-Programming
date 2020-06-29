import psycopg2
import csv

# Maakt een conectie met de DB
c = psycopg2.connect("dbname=sp user=postgres password=Jopa2002jp")
cur = c.cursor()
cur.execute("DROP TABLE IF EXISTS user_rec CASCADE")
cur.execute("""CREATE TABLE user_rec
                (id VARCHAR, u1 VARCHAR, u2 VARCHAR, u3 VARCHAR, u4 VARCHAR, u5 VARCHAR, u6 VARCHAR, u7 VARCHAR,
                u8 VARCHAR, u9 VARCHAR, u10 VARCHAR, u11 VARCHAR, u12 VARCHAR, u13 VARCHAR, u14 VARCHAR, u16 VARCHAR, 
                u17 VARCHAR, u18 VARCHAR, u19 VARCHAR, u20 VARCHAR, u21 VARCHAR, u22 VARCHAR)""")

# Maakt csv bestand aan
def create_csv(fieldname, filename):
    with open('csv/' + filename + '.csv', mode='w', newline="") as csv_file:
        csv_write = csv.DictWriter(csv_file, fieldnames=fieldname)
        csv_write.writeheader()


# Schrijft alle tabellen naar een csv bestand (wordt opgeslagen onder ../csv/)
def write_csv(filename, line):
    with open('csv/' + filename + '.csv', mode='a', newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(line)

# Kijkt welke producten overeenkomen
def match_products():
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    dictionary = {}
    for item in data:
        for item_2 in data:
            if item[3: 6] == item_2[3: 6]:
                if item[0] in dictionary:
                    dictionary[item[0]] += [item_2[0]]
                else:
                    dictionary.update({item[0]: [item[0]]})
                    dictionary[item[0]] += [item_2[0]]
        write_csv('products_rec', dictionary[item[0]][0: 23])
        dictionary.__delitem__(item[0])
        list.remove(data, item)


# kijkt welke gebruikers dezelfde producten gekocht hebben
def sort_user():
    cur.execute("SELECT * FROM profiles_previously_viewed")
    data = cur.fetchall()
    dictionary = {}
    for item in data:
        for item_2 in data:
            if item[1] == item_2[1]:
                if item[1] in dictionary:
                    dictionary[item[1]] += [item_2[0]]
                else:
                    dictionary.update({item[1]: [item[1]]})
                    dictionary[item[1]] += [item_2[0]]
                list.remove(data, item_2)
        if len(dictionary[item[1]]) < 23:
            for value in range(22 - len(dictionary[item[1]])):
                dictionary[item[1]] += [None]
        write_csv('user_rec', dictionary[item[1]][0: 22])
        dictionary.__delitem__(item[1])


# kijkt hoevaak gebruikers hetzelfde product gekocht hebben
def link_users():
    cur.execute("""SELECT * FROM user_rec""")
    data = cur.fetchall()
    dictionary = {}
    for item in data:
        for index in range(1, 22):
            for sIndex in range(1, 22):
                if (item[index] != item[sIndex]) and (item[index] is not None) and (item[sIndex] is not None):
                    if item[index] in dictionary:
                        if item[sIndex] in dictionary[item[index]]:
                            dictionary[item[index]][item[sIndex]] += 1
                        else:
                            dictionary[item[index]].update({item[sIndex]: 1})
                    else:
                        dictionary.update({item[index]: {item[sIndex]: 1}})
        list.remove(data, item)

    for user in dictionary:
        for profile in dictionary[user]:
            write_csv('compatibility', [user, profile, dictionary[user][profile]])


create_csv(['id', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
            'p16', ' p17', 'p18', 'p19', 'p20', 'p21', 'p22'], 'products_rec')
create_csv(['id', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9', 'u10', 'u11', 'u12', 'u13', 'u14', 'u15',
            'u16', 'u17', 'u18', 'u19', 'u20', 'u21', 'u22'], 'user_rec')
create_csv(['id', 'profile', 'compatibility'], 'compatibility')
match_products()
sort_user()

with open('csv/user_rec.csv') as csvfile:
    print("Copying {}...".format('user_rec'))
    cur.copy_expert("COPY " + "user_rec" + " FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
    c.commit()

link_users()
