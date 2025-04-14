myString = input("Type your sentence > ")
print()
for letter in myString:
  if letter.lower() == "b":
    print("\033[34m", end="")
  elif letter.lower() == "r":
    print("\033[31m", end="") 
  elif letter.lower() == "y":
    print("\033[33m", end="")
  print(letter, end="")
  