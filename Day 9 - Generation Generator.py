print("Generation Identifier")
print("")
yearBorn = int(input("Which year were you born? "))
print("")
if yearBorn <= 1900:
  print("Lost Generation")
elif yearBorn >= 1901 and yearBorn <= 1927:
  print("Greatest Generation")
elif yearBorn >= 1928 and yearBorn <= 1945:
  print("Silent Generation")
elif yearBorn >= 1946 and yearBorn <= 1964:
  print("Baby Boomers")
elif yearBorn >= 1965 and yearBorn <= 1980:
  print("Generation X")
elif yearBorn >= 1981 and yearBorn <= 1994:
  print("Millennials - the best generation")
elif yearBorn >= 1995 and yearBorn <=1995:
  print("Millennials - the best generation")
  ninetyFive = input("Are you born in '95? ")
  if ninetyFive == "yes" or ninetyFive == "Yes":
    print("That's the creme de la creme my friend!!!")
elif yearBorn == 1996 and yearBorn == 1996:
  print("Millennials - the best generation")
elif yearBorn >= 1981 and yearBorn <= 1996:
  print("Millennials - the best generation")
elif yearBorn >= 1997 and yearBorn <= 2012:
  print("Generation Z")
else:
  print("Generation Alpha")