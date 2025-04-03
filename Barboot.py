import random

print("Hai sa dam o gheara")



def diceRoll(sides):
  result = random.randint(1,sides)
  return result


p1Score = 0
p2Score = 0
for round in range (1,30):
  print("Round", round)
  p1dice1 = diceRoll(6)
  p1dice2 = diceRoll(6)
  print("Player 1 rolled", p1dice1, "and", p1dice2)
  print()
  p1diceTotal = p1dice1 + p1dice2
  
  print()
  
  p2dice1 = diceRoll(6)
  p2dice2 = diceRoll(6)
  print("Player 2 rolled", p2dice1, "and", p2dice2)
  print()
  p2diceTotal = p2dice1 + p2dice2
  
  
  if p1diceTotal > p2diceTotal:
    print("Player 1 wins")
    p1Score = p1Score + 1
    p2Score = p2Score + 0
    print("Player 1 Score: \n",p1Score)
    print("Player 2 Score: \n",p2Score)
    print()
    print()
    print()
    if p1Score == 5:
      print("Player 1 wins the game")
      exit()
  
  elif p1diceTotal < p2diceTotal:
    print("Player 2 wins")
    p1Score = p1Score + 0
    p2Score = p2Score + 1
    print("Player 1 Score: \n",p1Score)
    print("Player 2 Score: \n",p2Score)
    print()
    print()
    print()
    if p2Score == 5:
      print("Player 2 wins the game")
      exit()
  
  elif p1diceTotal == p2diceTotal:
    print("It's a draw")
    p1Score = p1Score + 0
    p2Score = p2Score + 0
    print("Player 1 Score: \n",p1Score)
    print("Player 2 Score: \n",p2Score)
    print()
    print()
    print()

  


