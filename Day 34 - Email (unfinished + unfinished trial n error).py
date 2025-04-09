import random, os, time
listOfEmail = []

def prettyPrint():
  
  for index in range(len(listOfEmail)):
    print(f"{index}. {listOfEmail[index]}")

def prettyPrint2(color):
  if color == "red":
    return "\033[91m"
  elif color == "green":
    return "\033[92m"
  elif color == "reset":
    return "\033[0m"


    print(f"Dear {email} we just want you to know this is a spam. But don't worry we will not spam you anymore.")
  
    print(f"Dear {email} sorry in advance for spamming you. I'm just testing my Python Code and you were on the wrong place at the wrong time.")
  
    print(f"Dear {email} This is spam. But this is also a test Best Regards.")
  
    print(f"Dear {email} This is spam. But this is also a a fake address.")

    print(f"Dear {email} If you are not a real person - is it fair to say that I didn't spam anybody?")
  
    print(f"Dear {email} Halfway spamming is not spamming, rightO?.")

    print(f"Dear {email} I'm sorry for spamming you. I'm just testing my Python Code. It won't happen again... unless you are in the loop :))).")
  
    print(f"Dear {email} Running out of ideas for spam emails.")
  
    print(f"Dear {email} HAVE you ever used AI to spam people? I think I will do that in the future")
 
    print(f"Dear {email} I'm sorry for spamming you again and again")
  
    print(f"Dear {email} This is the last spam email on the list I promise.")


#def getSpamming():
 # counter = 0
  #for email in listOfEmail:
   # print(f"{counter}. {email}")
   # counter += 1
   # print(f"Spam {counter} sent to {email}")
   # emails()
    

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
    prettyPrint()
    if email == 0:
      print("Email 0")
      print(f"Dear {email} we just want you to know this is a spam. But don't worry we will not spam you anymore.")
    elif email == 1:
      print("Email 1")
      print(f"Dear {email} sorry in advance for spamming you. I'm just testing my Python Code and you were on the wrong place at the wrong time.")
    elif email == 2:
      print("Email 2")
      print(f"Dear {email} This is spam. But this is also a test Best Regards.")

  
  
 