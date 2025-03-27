import random
correct_answer = random.randint(1,1000001)
print("Welcome to the guessing game! Can you guess the number I chose?")
print("Slice of advice: it is between 1 and 1,000,000")
hint_range_start = (correct_answer // 1000) * 1000
hint_range_end = hint_range_start + 999
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
    
    if failed_attempts >= 8:
      print("The number is between the ", hint_range_start, "and", hint_range_end, "range")
    print()
    users_pick = int(input("Retake your pick here: "))
    round += 1
  elif users_pick > correct_answer:
    print("Round: ", round)
    print("Too high")
    failed_attempts += 1
    print("Number of failed attempts: ", failed_attempts)
    
    if failed_attempts >= 8:
      print("The number is between the ", hint_range_start, "and", hint_range_end, "range")
    print()
    users_pick = int(input("Retake your pick here: "))
    round += 1
  elif users_pick == correct_answer:
    print("Round: ", round)
    print("You got it!")
    print("Number of failed attempts before succeeding: ", failed_attempts)
    exit()