import os, time

inventory = []

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    print()
    print("Welcome!")

while True:
    print("INVENTORY")
    print("=========")

    choice = input("1. Add\n2. View\n3. Remove\n> ")
    if choice == "1":
        item = input("What's the name of the item you want to add?\n> ")
        inventory.append(item.capitalize())
        print(f"{item.capitalize()} has added on the list.")
        print()
        time.sleep(3)
        os.system("cls")
    elif choice == "2":
        while True:
            newChoice = input("1. See items w/o duplicates\n2. See all items.\n3. See how many times the items appear\n> ")
            if newChoice == "1":
                for items in inventory:
                    if inventory.count(items) == 1:
                        print(items)
                print()
                time.sleep(3)
                os.system("cls")
                break
            elif newChoice == "2":
                for items in inventory:
                    print(items)
                print()
                time.sleep(3)
                os.system("cls")
                break
            elif newChoice == "3":
                for items in inventory:
                    print(f"{items} appears in the Inventory list {inventory.count(items)} time(s)!")
                print()
                time.sleep(3)
                os.system("cls")
                break
            else:
                print("Please choose accordingly")
                time.sleep(3)
                os.system("cls")
                continue

    elif choice == "3":
        item = input("What's the name of the item you want to remove?\n")
        inventory.remove(item.lower().capitalize())
        print(f"{item.capitalize()} has been removed from the list.")
        time.sleep(3)
        os.system("cls")
    else:
        print("Please choose a valid option from above")
        print()
        time.sleep(3)
        os.system("cls")

    

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()

