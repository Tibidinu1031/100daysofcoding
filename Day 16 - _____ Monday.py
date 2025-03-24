counter = 0
quote = "Guess the saying: _____ Monday!!!"
while True:
  print(quote)
  guess = input("Enter your guess: ")
  if guess == "happy" or guess == "Happy":
    print("Correct!")
    print("You got it right after ", counter, " failed attempts")
    break
  else:
    print("Try again!")
    counter += 1
    print("Number of incorrect attempts: ", counter)
print("Congratulations! You guessed it!")

