from replit import db
import datetime, os, time


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


password = input("This doc is password protected. Please enter the password > ")
if password != "1234":
  print("--------------")
  print("Wrong password")
  exit()
else:
  print("Welcome to the database")
  print()
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
      