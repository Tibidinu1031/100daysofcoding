print("People List")
list = []

def prettyPrint():
  for index in range(len(list)):
    print(f"{index + 1}. {list[index]}")
    

while True:
  firstName = input("What is your first name? ")
  lastName = input("What is your last name? ")
  print()
  fullName = (f"{firstName.strip().title()} {lastName.strip().title()}")
  print(f"Your name is {fullName}.")
  print()
  if fullName in list:
    print(f"{fullName} has already been added to the list.")
  else:
    list.append(fullName)
    prettyPrint()
  print("---------------------------------------")
  print()