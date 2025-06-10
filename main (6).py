import random

while True:
  print("HIGH SCORES")
  print()
  name = input("What is your name? ")
  score = random.randint(1, 100000)
  playAgain = input("Do you want to play again? (Y/N) ")

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()
  
  if playAgain.lower() == "n":
    break
  elif playAgain.lower() == "y":
    continue
  

  
  