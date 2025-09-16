from replit import db
import datetime, os, time

def addTweet():
  tweet = input("enter your tweet:> ")
  print("Tweet added!")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet

def viewTweets():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(i, " -- " ,db[i])
    print()
    counter += 1
    if counter % 10 == 0:
      moreTweets = input("1. View more tweets\n2. Back to menu\n> ")
      if moreTweets == "2":
        break

while True:
  print("Tweeter")
  print("=======")
  print()

  menu = input("1. Add Tweet\n2. View Tweets\n> ")
  if menu == "1":
    addTweet()
    time.sleep(1.5)
    os.system("clear")
  if menu == "2":
    viewTweets()
    time.sleep(4)
    os.system("clear")      