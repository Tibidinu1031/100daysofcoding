import random

print("Hangman Game")
print()
list_of_words = ["random", "sports", "entrepreneurship", "neuroscience", "leadership", "sociology", "psychology", "biology", "physics", "mathematics", "engineering", "medicine", "law", "economics", "history"]
randomWord = random.choice(list_of_words)
correctLetters = []
wrongLetters = []
lives = 6

print(randomWord)
randomWordListChangeable = list(randomWord)
fixedRandomWordList = list(randomWord)



while True:
  
  print()
  choice = input("Choose a letter: ")
  
  if choice in randomWord:
    print("Correct! Keep it up!")
    print(f"Lives left: {lives}")
    correctLetters.append(choice)
    print(f"Correct letters: {correctLetters}")
    randomWordListChangeable.remove(choice)
    if choice not in randomWordListChangeable and choice in correctLetters:
      print(f"You already used {choice}!")
    elif choice in randomWordListChangeable and choice not in correctLetters:
      print("Wrong choice")
      lives -= 1
      print(f"Lives left: {lives}")
    
    if len(randomWordListChangeable) == 0:
      print("You win!")
      break
  elif choice not in randomWord:
    wrongLetters.append(choice)
    print(f"Wrong letters: {wrongLetters}")
    print("Wrong!")
    lives -= 1
    print(f"Lives left: {lives}")
    if lives == 0:
      print("You lose!")
      break