print("REPLIT LOGIN SYSTEM")
print()
def login():
  username = input("What's your username?: ")
  password = input("What's your password?: ")
  if username == "TiberiusDinu" and password == "co-founder&CEO":
    print("Welcome to REPLIT!")
    exit()
  else:
    print("Whoops! I don't recognize that username or password. Try again!")
  

while True:
  login()

