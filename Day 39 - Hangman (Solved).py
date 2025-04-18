import random

listOfWords = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
lettersPicked = []
word = random.choice(listOfWords)
lives = 6
print(word)
while True:
  letter = input("Pick a letter: ")

  if letter in lettersPicked:
    print("You already picked that letter.")

  lettersPicked.append(letter)

  if letter in word:
    print("You got a letter!")
  else:
    print("Wrong guess.")
    lives -= 1
    print("You have", lives, "lives left.")

  allLetters = True
  for i in word:
    if i not in lettersPicked:
      print("_", end="")
      
      allLetters = False
    else:
      print(i, "", end="")
  print()    

  if allLetters:
    print("\nYou won!")
    break

  if lives <= 0:
    print("\nYou lost!")
    print(f"The word was --> {word}")
    break

