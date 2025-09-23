from replit import db
import datetime, os, time, random, hashlib


rightUser = True


def addJournalEntry():
  entry = input("Enter your journal entry > ")
  print("Entry saved in the database!")
  print()
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  key = f"entry{timestamp}"
  db[key] = entry


def viewJournalEntries():
  matches = db.prefix("entry")
  matches = matches[::-1]
  if not matches:
    print("No entries found.")
    return
  for i, key in enumerate(matches):
    print(f"{key} --> {db[key]}")
    print()
    if i == len(matches) - 1:
      print("That's it! No more entries!")
      break
    nextOne = input("Do you want to see the next entry? (y/n) > ")
    if nextOne.lower() == "n":
      break
    else:
      continue


def createUser():
  username = input("Enter a username > ")
  password = input("Enter a password > ")
  salt = random.randint(1000, 9999)
  newPass = f"{password}{salt}"
  newPass = hashlib.sha256(newPass.encode()).hexdigest()

  db[username] = {'password': newPass, 'salt': salt}

  print("User created successfully!")
  print()


def login():
  global rightUser
  username = input("Enter your username > ")
  password = input("Enter your password > ")
  keys = db.keys()
  if username not in db:
    print("Login failed. Please try again.")
    print()
    rightUser = False
    return
    
  salt = db[username]['salt']
  newPass = f"{password}{salt}"
  newPass = hashlib.sha256(newPass.encode()).hexdigest()

  if newPass == db[username]['password']:
    print(f"Login successful! Welcome {username}!")
    print()
    rightUser = True
  else:
    print("Login failed. Please try again.")
    print()
    rightUser = False

      
keys = db.keys()
if len(keys) == 0:
  print("Welcome to your journal! Please add a user and a password to get started.")
  createUser()
else:
  print("Welcome back to your journal! Please log in to continue.")


count = 0
while True:
  login()
  if rightUser:
    break
  else:
    count += 1
    if count == 3:
      print("Too many failed login attempts. Exiting...")
      exit()
    continue


while True:
  choice = input("1. Add journal entry\n2. View journal entries\n3. Exit\nEnter your choice > ")
  if choice == "1":
    addJournalEntry()
    time.sleep(1)
    os.system("clear")
  elif choice == "2":
    print("Here's your previous journal entry: ")
    viewJournalEntries()
    time.sleep(4)
    os.system("clear")
  elif choice == '3':
    print("Exiting...")
    exit()
