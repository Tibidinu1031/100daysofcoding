from replit import db
import random, os, time, hashlib


def createUser():
  time.sleep(0.5)
  os.system("clear")
  username = input("Enter username: ")
  password = input("Enter password: ")
  keys = db.keys()
  if username in keys:
    print("Username already exists. Please choose a different one.")
    return

  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hashlib.sha256(newPassword.encode()).hexdigest()
  
  db[username] = {"password": newPassword, "salt": salt}

  print(f"{username} added successfully!")


def login():
  time.sleep(0.5)
  os.system("clear")
  username = input("Enter username: ")
  password = input("Enter password: ")
  keys = db.keys()
  if username not in keys:
    print("Username not found. Please add one.")
    return

  salt = db[username]['salt']
  newPassword = f"{password}{salt}"
  newPassword = hashlib.sha256(newPassword.encode()).hexdigest()

  if db[username]["password"] == newPassword:
    print(f"Login Successful. Welcome {username}!")
    time.sleep(2)
    os.system("clear")
  else:
    print("Invalid username or password. Please try again.")
    time.sleep(2)


while True:
  print("Welcome to the Login/Signup Page!")
  print()
  choice = input("1. Add User\n2. Login\n3. Exit\n4. See\n:> ")
  if choice == "1":
    createUser()
  elif choice == "2":
    login()
  elif choice == "3":
    print("Goodbye!")
    break
  elif choice == "4":
    keys = db.keys()
    if len(keys) == 0:
      print("No users found.")
    else:
      for key in db.keys():
        print(key, db[key])
  else:
    print("Invalid choice. Please try again.")
    continue

