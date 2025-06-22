import os, time

orders = []

types = {"Marinara" : 10, "Margherita" : 12, "Salami" : 14 }
toppings = {"Extra Mozarella" : 2.5, "Extra Salami" : 3.5}


while True:
    print()
    print("Pizzeria Da Tiberius")
    print("---------------")
    print()

    addView = input("1. Add Pizza(s)\n2. View Pizza(s)\n> ")
    if int(addView) == 1:
        print("Our menu is very simple yet very qualitative. Please check the pizzas below:")
        for keys in types:
            print(f"{keys:<12} ---> {types[keys]}$") 
        print()
        pizzaChoice = input("What pizza do you want to order?\n> ")
    elif addView == "2":
        print("Update code")
    time.sleep(3)
    os.system("cls")

    name = input("What's your name?\n> ")
    wantToppings = input("Do you want toppings?\n1. Yes\n2. No\n> ") # As a Neapolitan Pizza guy I am well aware of the fact that this line is blasphemy but I have a code exercise I need to finish.
    if wantToppings == "1":
        for keys in toppings:
            print(f"{keys:<16} ---> {toppings[keys]}$")
            
    elif wantToppings == "2":
        print("Wise choice my friend! You're a Neapolitan Pizza afficionado!")
    size = input("What size?\n1. S\n2. N (Normal)\n> ")
    quantity = input("How many do you want?\n> ")
    total = types[pizzaChoice] * toppings[wantToppings] * quantity
    print(f"TEST: Total = {total}") 
    nameList = [f"Name: {name}, Pizza(s): {pizzaChoice},Toppings: {wantToppings},Size: {size},Quantity: {quantity}, Total: {total}$"]
    orders.append(nameList)
    print(orders)
    time.sleep(3)
    os.system("cls")

