import os, time

orders = []

pizzas = ["Marinara", "Margherita", "Salami"]
toppings = ["Extra Mozarella", "Extra Salami", "Extra Prosciutto"]

pizzaValue = 0
toppingValue = 0

while True:
  print()
  print("Pizzeria Da Tiberius")
  print("---------------")
  print()
  
  print("Our menu is shown below:")
  print(f"Small {pizzas[0]:<11} ---> $10 | Big {pizzas[0]:<11} ---> $20")
  print(f"Small {pizzas[1]:<11} ---> $12 | Big {pizzas[1]:<11} ---> $22")
  print(f"Small {pizzas[2]:<11} ---> $14 | Big {pizzas[2]:<11} ---> $24")
  print("----------------------")
  print("Toppings below:")
  for items in toppings:
    print(items, "\n", end="")
  
  
  print()
  print("1. Add Pizza(s)")
  print("2. View Pizzas")
  
  choice = input("> ")
  if choice == "2":
    print(orders)
  elif int(choice) == 1:
    name = input("What's your name\n> ")
    pizza = input("What pizza do you want?\n> ")
    if pizza.lower() == "marinara":
      pizzaValue = 10
      print(f"Test: Value: {pizzaValue}")
    elif pizza.lower() == "margherita":
      pizzaValue = 12
      print(f"Test: Value: {pizzaValue}")
    elif pizza.lower() == "salami":
      pizzaValue = 14
      print(f"Test: Value: {pizzaValue}")  
    toppingsAgain = input("What toppings do you want\n> ")
    if toppingsAgain.lower() == "extra mozarella":
      toppingValue += 5
    elif toppingsAgain.lower() == "extra salami":
      toppingValue += 6
    elif toppingsAgain.lower() == "extra prosciutto":
      toppingValue += 7
    size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
    if size.lower() == "big":
      pizzaValue += 10
      print(f"Test: PizzaValue = {pizzaValue}")
    quantity = input("How many\n> ")
    total = (pizzaValue * int(quantity)) + toppingValue
    orderPerCustomer = [name, pizza, size, toppingsAgain, total]
    orders.append(orderPerCustomer)

    print("--------------")
    print(orders)
    print(f"Total = {total}$")
    print(total)
    print("--------------")
    
    oneMoreTime = input("Continue?\n 1. Yes\n2. No\n> ")
    if oneMoreTime == "1":
      continue
    else:
      print("Done with the orders for today")
      break