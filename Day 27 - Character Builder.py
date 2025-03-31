import random, os, time

title = "Character Builder"
print(title)
print("")
characterName = ""
characterType = ""
character_health = ""
character_strength = ""
while True:
  def diceRoll1():
    six_sided_dice = random.randint(1, 6)
    start = input("Welcome! Please press Enter to start: ")
    if start == "":
      characterName = input("Name your Legend: ")
      characterType = input("Character Type (Human, Elf, Wizard, Orc): ")
      print("Now let's calculate " + characterName + " the " + characterType + "'s health by rolling 2 dices. Good luck:")
      time.sleep(4)
      os.system("clear")
      print("First dice roll is:")
      print(int(six_sided_dice))
      time.sleep(2)
      os.system("clear")
      print(title + "\n")
      twelve_sided_dice = random.randint(1, 12)
      print("Second dice roll is")
      print(int(twelve_sided_dice))
      time.sleep(2)
      os.system("clear")
      print(title + "\n")
      print("The characater's health is: ")
      health = ((six_sided_dice * twelve_sided_dice) / 2) + 10
      print(health)
      return health
     
  character_health = diceRoll1()
  
  
  def diceRoll2():
    six_sided_dice = random.randint(1, 6)
    eight_sided_dice = random.randint(1, 8)
    start = input("Now it's time to calculate the character's strength. Please press Enter to start: ")
    if start == "":
      print("The character's strenth will also be decided by 2 roles of a dice:")
      time.sleep(4)
      os.system("clear")
      print("First dice roll is:")
      print(int(six_sided_dice))
      time.sleep(2)
      os.system("clear")
      print(title + "\n")
      twelve_sided_dice = random.randint(1, 12)
      print("Second dice roll is")
      print(int(eight_sided_dice))
      time.sleep(2)
      os.system("clear")
      print(title + "\n")
      print("The characater's strength is: ")
      strength = ((six_sided_dice * eight_sided_dice) / 2) + 10
      print(strength)
      return strength
      
      
  character_strength = diceRoll2() 
  
  
  print("To sum it up, your character's name is " + characterName + ", and he is a " + characterType)
  print("Health: " + str(character_health))
  print("Strength: " + str(character_strength))
  time.sleep(5)
  os.system("clear")
  restart = input("Do you want to create another character? ")
  if restart == "yes":
      def diceRoll1():
        six_sided_dice = random.randint(1, 6)
        start = input("Welcome! Please press Enter to start: ")
        if start == "":
          characterName = input("Name your Legend: ")
          characterType = input("Character Type (Human, Elf, Wizard, Orc): ")
          print("Now let's calculate " + characterName + " the " + characterType + "'s health by rolling 2 dices. Good luck:")
          time.sleep(4)
          os.system("clear")
          print("First dice roll is:")
          print(int(six_sided_dice))
          time.sleep(2)
          os.system("clear")
          print(title + "\n")
          twelve_sided_dice = random.randint(1, 12)
          print("Second dice roll is")
          print(int(twelve_sided_dice))
          time.sleep(2)
          os.system("clear")
          print(title + "\n")
          print("The characater's health is: ")
          health = ((six_sided_dice * twelve_sided_dice) / 2) + 10
          print(health)
          return health

      character_health = diceRoll1()


      def diceRoll2():
        six_sided_dice = random.randint(1, 6)
        eight_sided_dice = random.randint(1, 8)
        start = input("Now it's time to calculate the character's strength. Please press Enter to start: ")
        if start == "":
          print("The character's strenth will also be decided by 2 roles of a dice:")
          time.sleep(4)
          os.system("clear")
          print("First dice roll is:")
          print(int(six_sided_dice))
          time.sleep(2)
          os.system("clear")
          print(title + "\n")
          twelve_sided_dice = random.randint(1, 12)
          print("Second dice roll is")
          print(int(eight_sided_dice))
          time.sleep(2)
          os.system("clear")
          print(title + "\n")
          print("The characater's strength is: ")
          strength = ((six_sided_dice * eight_sided_dice) / 2) + 10
          print(strength)
          return strength


      character_strength = diceRoll2() 


      print("To sum it up, your character's name is " + characterName + ", and he is a " + characterType)
      print("Health: " + str(character_health))
      print("Strength: " + str(character_strength))
      time.sleep(5)
      os.system("clear")
      restart = input("Do you want to create another character? ")
    

  

  elif restart == "no":
    print("Thank you for playing!")
    exit()
    
  