from replit import db
import random


def addUser():
  username = input("Enter username: ")
  password = input("Enter password: ")
  salt = str(random.randint(1000, 9999))
  hashed_password = hash(f"{password}{salt}")
  db[username] = {"hashed_password": hashed_password, "salt": salt}


def login():
  username = input("Enter username: ")
  password = input("Enter password: ")
  if username in db:
    salt = db[username]["salt"]
    if hash(f"{password}{salt}") == db[username]["hashed_password"]:
      print("Login successful!") 
    else:
      print("Login failed. Invalid username or password.")
  else:
    print("Login failed. Invalid username or password.")


while True:
  choice = input("1. Add User\n2. Login\n3. Exit\n:> ")
  if choice == "1":
    addUser()
  elif choice == "2":
    login()
  elif choice == "3":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
    continue

