exit = ""
while exit != "yes" and exit != "Yes":
  animalChoice = input("What animal do you want? ")
  if animalChoice == "cow" or animalChoice == "Cow":
    print("A cow goes moo.")
  if animalChoice == "dog" or animalChoice == "Dog":
    print("A cow goes woof.")
  if animalChoice == "cat" or animalChoice == "Cat":
    print("A cow goes meow.")
  else:
    animalChoice = input("You can only choose cow, dog, or cat for now. Which one do you want? > ")
    if animalChoice == "cow" or animalChoice == "Cow":
      print("A cow goes moo.")
    if animalChoice == "dog" or animalChoice == "Dog":
      print("A cow goes woof.")
    if animalChoice == "cat" or animalChoice == "Cat":
      print("A cow goes meow.")
  exit = input("Do you want to exit? > ")      
