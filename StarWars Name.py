import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("STAR WARS NAME GENERATOR")
print()
names = input("Enter your first name, last name, mother's maiden name and the city you were born in: ")

#print(f"{first_name.title()[:3]}{last_name.lower()[:2]} {mumMaidenName.title()[:2]}{city.lower()[-3:]}")
split_names = names.split()
starWarsName = f"{str(split_names[0][:3].title())}{str(split_names[1][:2].lower())} {str(split_names[2][:2].title())}{str(split_names[3][-3:].lower())}"
print(starWarsName)
  