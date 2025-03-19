print("So let's start with the basics")
print("")
your_name = input("What is your name? ")
your_age = input("What is your age? ")
your_favorite_food = input("What is your favorite food? ")

print("==============================")

print("\033[32mHello! So your name is \033[0m", your_name, " and you're ", your_age, " years old right? ", "Last but not least - ya fav food is ", your_favorite_food, " right?")

checkMark = input("Is this correct? ")
if checkMark == "Yes": print("Ok. Bye!")
else: print("Also ok bye!")
      












