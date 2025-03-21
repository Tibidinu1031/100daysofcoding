print("Tip Calculator")
print("")
print("")
doughSpent = float(input("How much is the bill? > "))
print("")
print("See the tip rates below: ")
if doughSpent <= 100:
  tip = 0.1
  print(tip)
elif doughSpent >= 101 and doughSpent <= 200:
  tip = 0.15
  print(tip)
else:
  tip = 0.2
  print(tip)
print("")
number_of_people = int(input("How many people are in your group? > "))
print("")
answer = (doughSpent * tip + doughSpent) / number_of_people
print(round(answer, 2))