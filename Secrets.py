import os, time

normal_secret = os.environ['normal']
admin_secret = os.environ['admin']

while True:
  chooseUser = input("1. Normal User\n2. Admin User\n> ")
  password = input("Enter password:> ")

  if chooseUser == "1":
    if password == normal_secret:
      print("Welcome Normal User")
      time.sleep(2)
      os.system("clear")
    else:
      print("Wrong Password")
      time.sleep(2)
      os.system("clear")

  if chooseUser == "2":
    if password == admin_secret:
      print("Welcome Admin User")
      time.sleep(2)
      os.system("clear")
    else:
      print("Wrong Password")
      time.sleep(2)
      os.system("clear")
  