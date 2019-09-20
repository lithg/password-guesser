import argparse

# ------------------------------------------

common_list = []
l33t_list = []
bds = []

global name
name = input("Victim's name: ")
name = name.lower()

surname = input("Victim's surname: ")
surname = surname.lower()

birthday =  input("Victim's birthday (DDMMYY): ")

global wife
wife = input("Victim's wife: ")
wife = wife.lower()

pet = input("Victim's pet's name: ")
pet = pet.lower()


common_list.append(name)
common_list.append(surname)
common_list.append(name + surname)
common_list.append(birthday)
common_list.append(wife)
common_list.append(pet)



birthday_dd = birthday[:-6]
birthday_mm = birthday[2:-4]
birthday_yy = birthday[6:]
birthday_yyyy = birthday[4:]

bds = [
    birthday_dd,
    birthday_mm,
    birthday_yy,
    birthday_yyyy

]

# ------------------------------------------

def commom_name():

    for i in bds:
        common_list.append(i)

    # name
    for i in bds:
        common_list.append(name + i)

    for i in bds:
        common_list.append(i + name)

    # surname

    for i in bds:
        common_list.append(surname + i)

    for i in bds:
        common_list.append(i + surname)

    # name + surname

    for i in bds:
        common_list.append(name + surname + i)

    for i in bds:
        common_list.append(i + name + surname)


    # pet

    for i in bds:
        common_list.append(pet + i)

    for i in bds:
        common_list.append(i + pet)

    file = open('wordlist.txt', 'a')

    for i in common_list:
        file.write(i + '\n')

    file.close()

# ------------------------------------------

def l33t_name():
    global name
    global wife

    # name
    if 'a' in name:
        name = name.replace('a', '4')
    
    if 'e' in name:
        name = name.replace('e', '3')

    if 'i' in name:
        name = name.replace('i', '1')

    if 'o' in name:
        name = name.replace('o', '0')

    if 't' in name:
        name = name.replace('t', '7')

    if 's' in name:
        name = name.replace('s', '5')


    # wife
    if 'a' in wife:
        wife = wife.replace('a', '4')
    
    if 'e' in wife:
        wife = wife.replace('e', '3')

    if 'i' in wife:
        wife = wife.replace('i', '1')

    if 'o' in wife:
        wife = wife.replace('o', '0')

    if 't' in wife:
        wife = wife.replace('t', '7')

    if 's' in wife:
        wife = wife.replace('s', '5')

    l33t_list.append(wife)

    for i in bds:
        l33t_list.append(wife + i)

    for i in bds:
        l33t_list.append(i + wife)


    file = open('wordlist.txt', 'a')

    for i in l33t_list:
        file.write(i + '\n')

    file.close()

# ------------------------------------------

if __name__ == "__main__":
    commom_name()
    l33t_name()
    print('Wordlist generated at: wordlist.txt')