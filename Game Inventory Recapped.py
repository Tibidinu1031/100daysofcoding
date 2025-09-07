print("Game Inventory Recap")
print("--------------------")
print()

inventory = []

try:
    f = open("inventory.txt", "r")
    inventory = (eval(f.read()))
    f.close()
except:
    print("No inventory found. Please add items!")
    print()

def prettyPrint():
    print()
    print(f"{"item":^15} {"quantity":^15}")
    for item in set(inventory):
        print(f"{item:^15} {inventory.count(item):^15}")
    print()

while True:
    choice = input("1. Add Item\n2. View Inventory\n3. Remove\n> ")
    if choice == "1":
        item = input("Enter item name: ")
        inventory.append(item)
        print(f"{item} added to inventory.")
        print()
    elif choice == "2":
        print("Displaying current inventory:")
        prettyPrint()
    elif choice == "3":
        removedItem = input("Enter item name to remove: ")
        if removedItem in inventory:
            inventory.remove(removedItem)
            print(f"{removedItem} removed from inventory.")
        else:
            print(f"{removedItem} not found in inventory.")
            

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()