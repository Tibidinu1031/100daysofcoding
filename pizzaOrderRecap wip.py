print("Pizza Order Recap")
print("------------------")
print()

orders = []

try:
    f = open("pizzaOrder.txt", "r")
    orders = eval(f.read())
    f.close()
except:
    print("Welcome to Python Pizza!")
    print()

name = ""
pizza = ""
topping = ""   

while True:
   choice = input("1. Add Pizza\n2. View Orders\n> ")
   if choice == "1":
      pizzaChoice = input("Choose a pizza from below:\n1. Salami\n2. Margherita\n3. Marinara\n> ")
      if pizzaChoice == "1":
         pizza = "Salami"
      elif pizzaChoice == "2":
         pizza = "Margherita"
      elif pizzaChoice == "3":
         pizza = "Marinara"
      else:
         print("Invalid choice, please try again.")

      toppingChoice = input("Choose a topping from below:\n1. Extra Salami\n2. Extra Mozarella\n3. Extra Olive Oil\n> ")
      if pizzaChoice == "1":
         topping = "Extra Salami"
      elif pizzaChoice == "2":
         pizza = "Extra Mozarella"
      elif pizzaChoice == "3":
         pizza = "Extra Olive Oil"
      else:
         print("Invalid choice, please try again.")

      name = input("Whose name is this order on?:> ")

      order = [name, pizza, topping]
      orders.append(order)
      f = open("pizzaOrder.txt", "w")
      f.write(str(orders))
      f.close()

   if choice == '2':
      print("The orders so far are listed below:")
      print(orders)








   










