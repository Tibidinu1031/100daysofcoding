import os, random, time

def diceRoll(sides):
  result = random.randint(1, sides)
  return result

def health():
  healthStatus = ((diceRoll(6) * diceRoll(12)) / 2) + 10
  return healthStatus

def strength():
  strengthStatus = ((diceRoll(6) * diceRoll(8)) / 2) + 12
  return strengthStatus



while True:
  print(" ⚔⚔ BATTLE TIME ⚔⚔ ")
  print()
  start = input("Press Enter to start: ")
  if start == "":
    # c1 = character 1
    c1Name = input("Name your Legend:\n ")
    print()
    c1Type = input("Character Type (Human, Elf, Wizard, Orc, etc.):\n")
    print()
    print("We'll throw 1 pair of dices twice to determine the Legend's health and strength.")
    print()
    print("Now we have all the details. Here's your Legend's full profile below: ")
    print("Charater Name:\n", c1Name)
    print()
    print("Character Type:\n", c1Type)
    print()
    c1Health = health()
    print("There we go --> Health = ", c1Health)
    c1Strength = strength()
    print("There we go --> Strength = ", c1Strength)
    print()
    print()
    print("Who is he or she battling?")
    print()

    # c2 = character 2
    c2Name = input("Name your Legend:\n ")
    print()
    c2Type = input("Character Type (Human, Elf, Wizard, Orc, etc.):\n")
    print()
    print("We'll throw 1 pair of dices twice to determine the Legend's health and strength.")
    print()
    print("Now we have all the details. Here's your Legend's full profile below: ")
    print("Charater Name:\n", c2Name)
    print()
    print("Character Type:\n", c2Type)
    print()
    c2Health = health()
    print("There we go --> Health = ", c2Health)
    c2Strength = strength()
    print("There we go --> Strength = ", c2Strength)
    print()
    print()
    showtime = input("Press Enter to start the battle: ")
    if showtime == "":
      print(" ⚔⚔ SHOWTIME ⚔⚔ ")
      print()
      def displayContender1():
        print(" RED CORNER: ")
        print("NAME:\n ",c1Name)
        print("TYPE:\n ",c1Type)
        print("HEALTH:\n ",c1Health)
        print("STRENGTH:\n ",c1Strength)

      displayContender1()     
      print()
      def displayContender2():
        print(" BLUE CORNER: ")
        print("NAME:\n ",c2Name)
        print("TYPE:\n ",c2Type)
        print("HEALTH:\n ",c2Health)
        print("STRENGTH:\n ",c2Strength)

      displayContender2() 
      print("To decide who's doing the damage, we'll play rounds of barbut(Romanian Dice)")
      
      for battleRound in range(100):
        
        
        def battle():
          print("ROUND ", battleRound)
          c1DiceRoll1 = random.randint(1,6)
          print(c1Name, c1Type, "rolled a ", c1DiceRoll1)
          c1DiceRoll2 = random.randint(1,6)
          print(c1Name, c1Type, "rolled a ", c1DiceRoll2)
          c1DiceRollTotal = c1DiceRoll1 + c1DiceRoll2
          print()
          c2DiceRoll1 = random.randint(1,6)
          print(c2Name, c2Type, "rolled a ", c2DiceRoll1)
          c2DiceRoll2 = random.randint(1,6)
          print(c2Name, c2Type, "rolled a ", c2DiceRoll2)
          c2DiceRollTotal = c2DiceRoll1 + c2DiceRoll2
          global c1Health, c2Health


          
          if c1DiceRollTotal > c2DiceRollTotal:
            damage = abs(c1Strength - c2Strength) + 1
            c1Health -= 0
            c2Health -= damage
            print(c1Name, c1Type, "did ", damage, "damage to ", c2Name, c2Type)
            print()
            print(c1Name, c1Type, "remaining health is:\n",c1Health)
            print(c2Name, c2Type, "remaining health is:\n",c2Health)
            print()
            if c2Health <= 0:
              print(c2Name, c2Type, "has died!")
              print(c1Name, c1Type, "has won the battle!")
              exit()
          elif c2DiceRollTotal > c1DiceRollTotal:
            damage = abs(c1Strength - c2Strength) + 1
            c1Health -= damage
            c2Health -= 0
            print(c2Name, c2Type ,"did ", damage, "damage to ", c1Name, c1Type)
            print()
            print(c1Name, c1Type, "remaining health is:\n",c1Health)
            print(c2Name, c2Type, "remaining health is:\n",c2Health)
            print()
            if c1Health <= 0:
              print(c1Name, c1Type, "has died!")
              print(c2Name, c2Type, "has won the battle!")
              exit()
          elif c1DiceRollTotal == c2DiceRollTotal:
            print("It's a draw!")
        battleRound += 1

        time.sleep(4)
        os.system("clear")
          
          
      
        if battle():
          break
        
  
        
        
      
      
    

