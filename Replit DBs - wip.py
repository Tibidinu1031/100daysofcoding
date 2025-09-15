from replit import db
import datetime

print("Tweeter")
print("-------")
print()

tweets = []
index = 0

while True:
  choice = input("1. Add Tweet\n2. View Tweets\n> ")
  if choice == "1":
    tweet = input("Kindly input your tweet below:\n> ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db[f"{'timestamp'}{index}"] = timestamp
    db[f"{'tweet'}{index}"] = tweet
    completeTweet = [db[f"{'timestamp'}{index}"], db[f"{'tweet'}{index}"]]
    tweets.append(completeTweet)
    index += 1
  elif choice == "2":
    print("Tweets")
    print("------")
    keys = db.keys()
    for key in keys:
      print(f"{key}: {db[key]}", end="")
      print("\n")