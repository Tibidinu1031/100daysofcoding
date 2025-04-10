import random, os, time
listOfEmail = []
emailList = ["we just want you to know this is a spam. But don't worry we will not spam you anymore.\n\n Best Regards", "sorry in advance for spamming you. I'm just testing my Python Code and you were on the wrong place at the wrong time.", "This is spam. But this is also a test Best Regards.", "This is spam. But this is also a a fake address.", "If you are not a real person - is it fair to say that I didn't spam anybody?", "Halfway spamming is not spamming, rightO?.", "I'm sorry for spamming you. I'm just testing my Python Code. It won't happen again... unless you are in the loop :))).", "Running out of ideas for spam emails.", "HAVE you ever used AI to spam people? I think I will do that in the future", "I'm sorry for spamming you again and again"]

def prettyPrint():

  for index in range(len(listOfEmail)):
    print(f"{index}. {listOfEmail[index]}")
print()
def prettyPrint3():

  for index in range(10):
    print(f"Email {index}")
    print()
    print(f"Dear {listOfEmail[index]}")
    print(f"{emailList[index]}")
    if index >= 10:
      break
    time.sleep(3)
    os.system("clear")
    




def prettyPrint2(color):
  if color == "red":
    return "\033[91m"
  elif color == "green":
    return "\033[92m"
  elif color == "reset":
    return "\033[0m"


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
    print(f"{prettyPrint2('green')}{email} has added to the list. {prettyPrint2('reset')}")
    prettyPrint()
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
      print(f"{prettyPrint2('red')} {email} has removed from the list. {prettyPrint2('reset')}")
      prettyPrint()
  elif menu == "3":
    if len(listOfEmail) == 0:
      print("-- There are no emails in your list. --")
    else:
      prettyPrint()
  elif menu == "4":
    prettyPrint3()
    
  time.sleep(3)
  os.system("clear")

