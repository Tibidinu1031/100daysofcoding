import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#print(len(letters))
shortLetters = []

print("STAR WARS NAME GENERATOR")

#def nonSenseName():
  
for i in range(5):
  i = random.randint(0,len(letters) - 1)
  shortLetters.append(letters[i])
  shortLettersToString = ''.join(shortLetters)
  

firstName = input("What's your first name? > ")
secondName = input("What's your second name? > ")
city = input("What city were you born in? > ")

starWarsName = (f"{firstName} {secondName} {shortLettersToString.lower()} {city}")
starWarsNameList = starWarsName.split()
print(starWarsNameList)
print(f"Your random string is {shortLettersToString}")
print(f"Your Star Wars name is {starWarsNameList[0][:3].title()}{starWarsNameList[1][:2].lower()} {starWarsNameList[2][0:2].title()}{starWarsNameList[3][-3:].lower()}")




   

