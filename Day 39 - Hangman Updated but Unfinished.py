import random

print("Hangman Game")
print()
list_of_words = ["random", "sports", "entrepreneurship", "neuroscience", "leadership", "sociology", "psychology", "biology", "physics", "mathematics", "engineering", "medicine", "law", "economics", "history"]
randomWord = random.choice(list_of_words)
correctLetters = []
wrongLetters = []
underlineList = []
lives = 6

print(randomWord)
randomWordList = list(randomWord)
print(randomWordList)


for underline in range(len(randomWordList)):
  underline = "_"
  underlineList.append(underline)
  



while True:
  underline = " ".join(underlineList)
  print(underline)
  choice = input("Choose a letter: ").lower()
  
  if choice in randomWord:
    print("Correct! Keep it up!")
    print(f"Lives left: {lives}")
    correctLetters.append(choice)
    #print(f"Correct letters: {correctLetters}")
    randomWordList.remove(choice)
    position = randomWord.index(f"{choice}") + 1
    underlineList[position - 1] = choice
    
    
    print(f"position {position}")
    print(f"Lives left: {lives}")
    print()
    if len(randomWordList) == 0:
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