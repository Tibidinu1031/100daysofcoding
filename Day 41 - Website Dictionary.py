import os, time

webDetails = {"name" : None, "url" : None, "desc" : None, "rating" : None}

print("Website Details")
print()

def webPrint():
  print("==============================================================")
  print("Website name: ", name)
  print("Website url: ", url)
  print("Website description: ", desc)
  print("Website rating: ", rating, "/ 5") 
  print(f"test: {webDetails}")

while True:
  name = input("what the name of the website? >> ")
  webDetails["name"] = name
  print()
  url = input("what the url of the website? >> ")
  webDetails["url"] = url
  print()
  desc = input("what the description of the website? >> ")
  webDetails["desc"] = desc
  print()
  rating = input("what the rating of the website from 1 to 5? >> ")
  webDetails["rating"] = rating
  print()
  webPrint() 
  time.sleep(5)
  os.system('clear')
  