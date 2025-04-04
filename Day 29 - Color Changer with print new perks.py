print("Super Subroutine")
print()

def changer(color, text):
  if color == "red":
    print("\033[31m", text, sep="", end="")
  elif color == "green":
    print("\033[32m", text, sep="", end="")
  elif color == "blue":
    print("\033[34m", text, sep="", end="")
  else:
    print("\033[0m", text, sep="", end="")

print("Now I can change the color of my text to ", end="")
changer("red", "red ")
changer("reset", "or to ")
changer("green", "green ")
changer("reset", "or to ")
changer("blue", "blue ")
changer("reset", "if I want to.")
