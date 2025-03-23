
print("E P I C    🗿 📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
playerOne = input("Player 1 > ")
print()
playerTwo = input("Player 2 > ")
print()
if (playerOne == "R" or playerOne == "🗿") and (playerTwo == "R" or playerTwo == "🗿"):
  print("You both picked Rock, that's a draw! my friends, try again!")
elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "P" or playerTwo == "📄"):
  print("You both picked Paper, that's a draw! my friends, try again!")
elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "S" or playerTwo == "✂️"):
  print("You both picked Scissors, that's a draw! my friends, try again!")
elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "P" or playerTwo == "📄"):
  print("Player 1's Rock is smothered by Player 2's Paper! Player 2 wins!")
elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "S" or playerTwo == "✂️"):
  print("Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "R" or playerTwo == "🗿"):
  print("Player 1's Paper smothers Player 2's Rock! Player 1 wins!")
elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "S" or playerTwo == "✂️"):
  print("Player 1's Paper is cut by Player 2's Scissors! Player 2 wins!")
elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "R" or playerTwo == "🗿"):
  print( "Player 1's Scissors are crushed by Player 2's Rock! Player 2 wins!")
elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "P" or playerTwo == "📄"):
  print("Player 1's Scissors cuts through Player 2's Paper!")
else:
  print("Are you sure? You can only choose R, P or S!")
  playerOne = input("Which one is gonna' be Player 1: R/P/S? > ")
  playerTwo = input("Which one is gonna' be Player 2: R/P/S? > ")
  if (playerOne == "R" or playerOne == "🗿") and (playerTwo == "R" or playerTwo == "🗿"):
    print("You both picked Rock, that's a draw! my friends, try again!")
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "P" or playerTwo == "📄"):
    print("You both picked Paper, that's a draw! my friends, try again!")
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "S" or playerTwo == "✂️"):
    print("You both picked Scissors, that's a draw! my friends, try again!")
  elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "P" or playerTwo == "📄"):
    print("Player 1's Rock is smothered by Player 2's Paper! Player 2 wins!")
  elif (playerOne == "R" or playerOne == "🗿") and (playerTwo == "S" or playerTwo == "✂️"):
    print("Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "R" or playerTwo == "🗿"):
    print("Player 1's Paper smothers Player 2's Rock! Player 1 wins!")
  elif (playerOne == "P" or playerOne == "📄") and (playerTwo == "S" or playerTwo == "✂️"):
    print("Player 1's Paper is cut by Player 2's Scissors! Player 2 wins!")
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "R" or playerTwo == "🗿"):
    print( "Player 1's Scissors are crushed by Player 2's Rock! Player 2 wins!")
  elif (playerOne == "S" or playerOne == "✂️") and (playerTwo == "P" or playerTwo == "📄"):
    print("Player 1's Scissors cuts through Player 2's Paper!")