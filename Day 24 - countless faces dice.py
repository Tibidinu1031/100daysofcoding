print("Infinity Dice")
print()

sides = int(input("How many sides?: "))
def rollDice(sides):
  while True:
    import random
    sideNumber = random.randint(1,sides)
    print("you rolled: ", sideNumber)
    question = input("Roll again? ")
    if question == "yes":
      continue
    elif question == "no":
      break
    else:
      question = input("it's a yes or no question. yes or no: ")
      if question == "yes":
        continue
      elif question == "no":
        break
      print("C'e fini la comedie!")
  print("C'e fini la comedie!")
rollDice(sides)
    