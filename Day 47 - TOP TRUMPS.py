import random, os, time

print("-- GoT TOP TRUMPS --")
print()
print("Values are between 1 and 200")
print("----------------------------")
print()

dex = {}

dex["Tyrion"] = {"Intelligence": 170, "Speed": 50, "Guile": 130, "Strength": 30}
dex["Jon"] = {"Intelligence": 120, "Speed": 180, "Guile": 0, "Strength": 150}
dex["Arya"] = {"Intelligence": 160, "Speed": 190, "Guile": 100, "Strength": 60}
dex["Cersei"] = {"Intelligence": 130, "Speed": 0, "Guile": 200, "Strength": 0}

myScore = 0
computerScore = 0

while True:
  print("Let's play TOP TRUMPS!!")
  print()
  print(f"Your score is {myScore} and the computer's score is {computerScore}")
  print()
  
  randomPick1 = random.choice(list(dex.keys()))
  if randomPick1 not in dex:
    print("Character not found, please try again.")
    print()
    continue
    
  randomPick2 = random.choice(list(dex.keys()))
  topic = input("Pick your attribute: ").title()
  while topic not in dex[randomPick1]:
    print("Attribute not found, please try again.")
    topic = input("Pick your attribute: ").title()
  print()
  print(f"You have picked: {randomPick1}")
  print(f"The computer has picked: {randomPick2}")
  print()
  
  print("Let's compare the two!!")
  print()
  
  print(f"{randomPick1}'s {topic} is {dex[randomPick1][topic]}")
  print(f"{randomPick2}'s {topic} is {dex[randomPick2][topic]}")
  print()
  
  if dex[randomPick1][topic] > dex[randomPick2][topic]:
    print("You win!")
    myScore += 1
    print(f"Your score is {myScore} and the computer's score is {computerScore}")
    print()
  elif dex[randomPick1][topic] < dex[randomPick2][topic]:
    print("Computer wins!")
    computerScore += 1
    print(f"Your score is {myScore} and the computer's score is {computerScore}")
    print()
  elif dex[randomPick1][topic] == dex[randomPick2][topic]:
    print("It's a draw!")
    print()

  if myScore == 3:
    print("You win the game!")
    break
  elif computerScore == 3:
    print("Computer wins the game!")
    break

  playAgain = input("Would you like to play again? (y/n): ")
  if playAgain[0].lower() == "n":
    print("Thanks for playing!")
    break
  elif playAgain[0].lower() == "y":
    time.sleep(0)
    os.system("clear")
    continue
  
  
      