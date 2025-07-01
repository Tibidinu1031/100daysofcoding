import random

randomNumber = random.randint(0, 21)
print("Random # = ", randomNumber)

def reverse(value):
  if value <= 0:
    print("Done")
    return
  else:
    for i in range(value):
      print("🔥", end="")
    print()
    reverse(value - 1)

reverse(randomNumber)