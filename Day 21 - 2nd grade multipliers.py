number = int(input("Enter a number that you want multiplied: "))
score = 0
for i in range(1,11):
  print(number, "x", i, "=")
  number_multiplied = number * i
  answer = int(input(" "))
  if answer == number_multiplied:
    print("Correct!")
    score += 1
    print("Your score is ",score)
  else:
    print("Incorrect! The answer is", number_multiplied)
    score += 0
    print("No points this round! Your score remains ",score)
  print()
print("You scored", score, "out of 10!")
if score == 10:
  print("You got a perfect score! Amazing!")
elif score >= 7 and score <=9:
  print("You did pretty good... for a second grader!")
elif score <=6:
  print("You probably need to look inward :))))). (Spoken with love)")