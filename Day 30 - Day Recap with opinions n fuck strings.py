opinion = ""
day = 1
for i in range(1, 32):
  print(f"Day {day}")
  opinion = input(f"What is your opinion on what you learn on day {day}? ")
  print(f"You said day {day} was {opinion} ")
  print("")
  day += 1
  