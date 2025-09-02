print("Full-ON Mokedex w/ 2D Dictionaries")
print()

mokedex = {}

def prettyPrint():
    print()
    print(f"{'Name':^15} | {'Type':^15} | {'HP':^15} | {'MP':^15} |")
    for key, value in mokedex.items():
        print(f"{key:^15}", end = " | ")
        for subkey, subvalue in value.items():
            print(f"{subvalue:^15}", end = " | ")
        print()
    print()
                

while True:
    choice = input("1. Add Beast\n2. Show Mokedex\n3. Exit\n> ")
    if choice == "1":
        print("Add your beast!")
        name = input("Name: ")
        type = input("Type: ")
        hp = input("HP: ")
        mp = input("MP: ")
        mokedex[name] = {"type": type, "hp": hp, "mp": mp}

    elif choice == "2":
        prettyPrint()

    elif choice == "3":
        print("Bye!")
        break