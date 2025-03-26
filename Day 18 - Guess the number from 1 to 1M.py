correct_answer = 1031
print("Welcome to the guessing game! Can you guess the number I chose?")
print("Slice of advice: it is between 1 and 1,000,000")
round = 1
users_pick = int(input("Take your pick here: "))
failed_attempts = 0
while True:
  print()
  print()
  if users_pick < 0:
    print("You are not funny.")
    exit()
  elif users_pick < correct_answer:
    print("Round: ", round)
    print("Too low")
    failed_attempts += 1
    print("Number of failed attempts: ", failed_attempts)
    print()
    users_pick = int(input("Retake your pick here: "))
    round += 1
    continue
  elif users_pick > correct_answer:
    print("Round: ", round)
    print("Too high")
    failed_attempts += 1
    print("Number of failed attempts: ", failed_attempts)
    print()
    users_pick = int(input("Retake you pick here: "))
    round += 1
    continue
  elif users_pick == correct_answer:
    print("Round: ", round)
    print("You got it!")
    print("Number of failed attempts before succeeding: ", failed_attempts)
    exit()