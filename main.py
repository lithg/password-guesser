common_list = []
l33t_list = []
bds = []

global name
name = input("Victim's name: ")
name = name.lower()
common_list.append(name)
birthday =  input("Victim's birthday (DDMMYY): ")

birthday_dd = birthday[:-6]
birthday_mm = birthday[2:-4]
birthday_yy = birthday[6:]
birthday_yyyy = birthday[4:]

bds = [
    birthday,
    birthday_dd,
    birthday_mm,
    birthday_yy,
    birthday_yyyy

]

def commom_name():

    for i in bds:
        common_list.append(i)

    for i in bds:
        common_list.append(name + i)

    for i in bds:
        common_list.append(i + name)

    file = open('wordlist.txt', 'a')

    for i in common_list:
        file.write(i + '\n')

    file.close()


def l33t_name():
    global name

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

    l33t_list.append(name)

    for i in bds:
        l33t_list.append(name + i)

    for i in bds:
        l33t_list.append(i + name)


    file = open('wordlist.txt', 'a')

    for i in l33t_list:
        file.write(i + '\n')

    file.close()


if __name__ == "__main__":
    commom_name()
    l33t_name()
    print('Wordlist generated at: wordlist.txt')