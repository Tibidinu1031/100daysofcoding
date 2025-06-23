import os, time

orders = []

pizzas = ["Marinara", "Margherita", "Salami"]
pizzaPerMenuValue = 10

toppings = ["Extra Mozarella", "Extra Salami", "Extra Prosciutto"]
toppingsPerMenuValue = 5


pizzaMarinaraValue = 0
pizzaMargheritaValue = 0
pizzaSalamiValue = 0


pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
toppingValue = 0
quantity = 0

while True:
  print()
  print("Pizzeria Da Tiberius")
  print("---------------")
  print()
  
  print("Our menu is shown below:")
  for items in pizzas:
    print(f"Small {items:<11} ---> ${pizzaPerMenuValue} | Big {items:<11} ---> ${pizzaPerMenuValue + 10}")
    pizzaPerMenuValue += 2
  pizzaPerMenuValue -=6
  print("---------------------------------------------------------------")
  for items in toppings:
    print(f"Small {items:<16} ---> ${toppingsPerMenuValue}")
    toppingsPerMenuValue += 1
  toppingsPerMenuValue -= 3
  
  print()
  print("1. Add Pizza(s)")
  print("2. View Pizzas")
  
  choice = input("> ")
  if choice == "2":
    if orders != []:
      print(orders)
    else:
      print("Empty List. Please place an order!")
  elif choice == "1":
    name = input("What's your name\n> ")
    print(f"Got it. What's your order {name}?")
    print()
    
    while True:


      pizza = input("What pizza do you want?\n> ")
      if pizza.lower() == "marinara":
        pizzaMarinaraValue += 10
        print(f"Test: {pizzaMarinaraValue}")
        quantityPer = input("How many?\n> ")
        quantity += int(quantityPer)
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          pizzaMarinaraValue += 10
          print(f"Test::: Pizza Marinara value = {pizzaMarinaraValue}")
          pizzaMarinaraValue *= int(quantityPer)
          print(f"Test: {pizzaMarinaraValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          pizzaMarinaraValue += 0
          pizzaMarinaraValue *= int(quantityPer)
          print(f"Test: {pizzaMarinaraValue}")
          print(f"{pizza.title()} small. You got it! ") 
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue 
        print() 
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()





      elif pizza.lower() == "margherita":
        pizzaMargheritaValue += 12
        print(f"Test: {pizzaMargheritaValue}")
        quantityPer = input("How many?\n> ")
        quantity += int(quantityPer)
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          pizzaMargheritaValue += 10
          print(f"Test::: Pizza Marinara value = {pizzaMarinaraValue}")
          pizzaMargheritaValue *= int(quantityPer)
          print(f"Test: {pizzaMargheritaValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          pizzaMargheritaValue += 0
          pizzaMargheritaValue *= int(quantityPer)
          print(f"Test: {pizzaMargheritaValue}")
          print(f"{pizza.title()} small. You got it! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        print()
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()



      elif pizza.lower() == "salami":
        pizzaSalamiValue += 14
        print(f"Test: {pizzaSalamiValue}")
        quantityPer = input("How many?\n> ")
        quantity += int(quantityPer)
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          pizzaSalamiValue += 10
          print(f"Test::: Pizza Marinara value = {pizzaMarinaraValue}")
          pizzaSalamiValue *= int(quantityPer)
          print(f"Test: {pizzaSalamiValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          pizzaValue += 10
          pizzaSalamiValue *= int(quantityPer)
          print(f"Test: {pizzaSalamiValue}")
          print(f"{pizza.title()} small. You got it! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        print()
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()




      elif choice not in pizzas:
        print("We don't have. Please check out our menu and choose accordingly")
        continue
      addAnother = input("Add another?\n1. Yes\n2. No\n> ")
      if addAnother == "1":
        continue
      else:
        break

    while True:  
      toppingsAgain = input("Toppings\n0. No Fucking Topics - I'm a Neapolitan Pizza Afficionado\n1. Extra Mozarella\n2. Extra Salami\n3. Extra Prosciutto\n> ")
      if toppingsAgain == "0":
        print("Yup! You really are and we congratulate you for that! Salve, nostro amico!")
        break
      elif toppingsAgain.lower() == "1":
        toppingValue += 5
        print("Added")
        print()
      elif toppingsAgain.lower() == "2":
        toppingValue += 6
        print("Added")
        print()
      elif toppingsAgain.lower() == "3":
        toppingValue += 7
        print("Added")
        print()
      else:
        print("We don't have that")
        print()
        continue
      addAnother = input("Add another?\n1. Yes\n2. No\n> ")
      if addAnother == "1":
        continue
      else:
        break

    #quantity = input("How many\n> ")
    #print("Noted")
    #print()
    total = pizzaValue + toppingValue
    print(f"Total = {total}$")
    orderPerCustomer = [f"Customer Name: {name}, Total Quantity: {quantity}, Pizza: {pizza}, Size: {size}, Toppings: {toppingsAgain}, Total: {total}"]
    orders.append(orderPerCustomer)

    print("--------------")
    print(f"TEST::::: Pizza Value = ${pizzaValue}| toppings Value = ${toppingValue} | Q = {quantity}")
    print("--------------")
    print("Today's Orders:")
    print(orders)
    print("--------------")
    
    pizzaMarinaraValue = 0
    pizzaMargheritaValue = 0
    pizzaSalamiValue = 0
    toppingValue = 0
    quantity = 0
    oneMoreTime = input("Continue?\n1. Yes\n2. No\n> ")
    if oneMoreTime == "1":
      continue
    else:
      print("Done with the orders for today")
      break
  
  else:
    print("You can only place an order or see the current ones")
    continue