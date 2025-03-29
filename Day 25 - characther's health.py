print("Character Stat Generator")
print()

choice = input("Let's warm up with a dice roll, shall we?! Kindly take a pick: ")
print("Don't worry, this won't impact your character's health!")
def diceRoll1(choice):
  import random
  dice1 = random.randint(1,int(choice))
  return dice1
#diceRoll2 = 0
dice1 = diceRoll1(choice)
print("You rolled", dice1)
print()
for i in range(100):
  characthersName = input("What is your character's name?: ")
  print("Your character's health is calculated by two rolls of a 6-sided dice and an 8-sided dice. The product of both dice is your character's health as shown below:")
  def diceRoll2():
    import random
    dice1 = random.randint(1,6)
    print("You rolled a", dice1)
    dice2 = random.randint(1,8)
    print("You rolled a", dice2)
    return dice2 * dice1
  characthersHealth = diceRoll2()
  if characthersHealth >= 40:
    print(f"Your character's health is \033[32m{characthersHealth}\033[0m")
  if characthersHealth >= 20 and characthersHealth <= 39:
    print(f"Your character's health is \033[33m{characthersHealth}\033[0m")
  if characthersHealth <= 19:
    print(f"Your character's health is \033[31m{characthersHealth}\033[0m")
  print()
  playAgain = input("Would you like to play again?: ")
  if playAgain == "yes":
    characthersName = input("What is your character's name?: ")
    
    def diceRoll2():
      import random
      dice1 = random.randint(1,6)
      print("You rolled a", dice1)
      dice2 = random.randint(1,8)
      print("You rolled a", dice2)
      return dice2 * dice1
    print("Your character's health is calculated by two rolls of a 6-sided dice and an 8-sided dice. The product of both dice is your character's health as shown below:")
    characthersHealth = diceRoll2()
    if characthersHealth >= 40:
      print(f"Your character's health is \033[32m{characthersHealth}\033[0m")
    if characthersHealth >= 20 and characthersHealth <= 39:
      print(f"Your character's health is \033[33m{characthersHealth}\033[0m")
    if characthersHealth <= 19:
      print(f"Your character's health is \033[31m{characthersHealth}\033[0m")
    print()
    playAgain = input("Would you like to play again?: ")
  elif playAgain == "no":
    print("Thank you for playing!")
    break
    
    




  