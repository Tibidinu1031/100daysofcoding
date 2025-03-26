from getpass import getpass as input

playerOneScore = 0
playerTwoScore = 0
round = 1
while True:
  print("E P I C    🗿 📄 ✂️    B A T T L E ")
  print()
  print("Round ", round)
  print()
  print("Select your move (R, P or S)")
  playerOne = input("Player 1 > ")
  print()
  playerTwo = input("Player 2 > ")
  print()
  if (playerOne == "R" or playerOne == "🗿") and (playerTwo == "R" or playerTwo == "🗿"):
    print("You both picked Rock, that's a draw! my friends, try again!")
    playerOneScore += 0
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "P" or playerTwo == "📄"):
    print("You both picked Paper, that's a draw! my friends, try again!")
    playerOneScore += 0
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "S" or playerTwo == "✂️"):
    print("You both picked Scissors, that's a draw! my friends, try again!")
    playerOneScore += 0
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "P" or playerTwo == "📄"):
    print("Player 1's Rock is smothered by Player 2's Paper! Player 2 wins!")
    playerOneScore += 0
    playerTwoScore += 1
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "S" or playerTwo == "✂️"):
    print("Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
    playerOneScore += 1
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "R" or playerTwo == "🗿"):
    print("Player 1's Paper smothers Player 2's Rock! Player 1 wins!")
    playerOneScore += 1
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "S" or playerTwo == "✂️"):
    print("Player 1's Paper is cut by Player 2's Scissors! Player 2 wins!")
    playerOneScore += 0
    playerTwoScore += 1
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "R" or playerTwo == "🗿"):
    print("Player 1's Scissors are crushed by Player 2's Rock! Player 2 wins!")
    playerOneScore += 0
    playerTwoScore += 1
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "P" or playerTwo == "📄"):
    print("Player 1's Scissors cuts through Player 2's Paper!")
    playerOneScore += 1
    playerTwoScore += 0
    round += 1
    print("Player One Score: ", playerOneScore)
    print("Player Two Score: ", playerTwoScore)
    if playerOneScore == 3:
      print("Player 1 has won the contest!")
      exit()
    elif playerTwoScore == 3:
      print("Player 2 has won the contest!")
      exit()
    else:
      continue

  else:
    print("Are you sure? You can only choose R, P or S!")
    playerOne = input("Which one is gonna' be Player 1: R/P/S? > ")
    playerTwo = input("Which one is gonna' be Player 2: R/P/S? > ")
    if (playerOne == "R" or playerOne == "🗿") and (playerTwo == "R" or playerTwo == "🗿"):
      print("You both picked Rock, that's a draw! my friends, try again!")
      playerOneScore += 0
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "P" or playerTwo == "📄"):
      print("You both picked Paper, that's a draw! my friends, try again!")
      playerOneScore += 0
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "S" or playerTwo == "✂️"):
      print("You both picked Scissors, that's a draw! my friends, try again!")
      playerOneScore += 0
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "P" or playerTwo == "📄"):
      print("Player 1's Rock is smothered by Player 2's Paper! Player 2 wins!")
      playerOneScore += 0
      playerTwoScore += 1
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "S" or playerTwo == "✂️"):
      print("Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
      playerOneScore += 1
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "R" or playerTwo == "🗿"):
      print("Player 1's Paper smothers Player 2's Rock! Player 1 wins!")
      playerOneScore += 1
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "S" or playerTwo == "✂️"):
      print("Player 1's Paper is cut by Player 2's Scissors! Player 2 wins!")
      playerOneScore += 0
      playerTwoScore += 1
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "R" or playerTwo == "🗿"):
      print("Player 1's Scissors are crushed by Player 2's Rock! Player 2 wins!")
      playerOneScore += 0
      playerTwoScore += 1
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue
    elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "P" or playerTwo == "📄"):
      print("Player 1's Scissors cuts through Player 2's Paper!")
      playerOneScore += 1
      playerTwoScore += 0
      round += 1
      print("Player One Score: ", playerOneScore)
      print("Player Two Score: ", playerTwoScore)
      if playerOneScore == 3:
        print("Player 1 has won the contest!")
        exit()
      elif playerTwoScore == 3:
        print("Player 2 has won the contest!")
        exit()
      else:
        continue