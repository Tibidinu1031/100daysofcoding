import os, time

firstPerson = {"name" : "", "DoB": "", "cell" : "", "email" : "", "address": ""}

print('==============================')
print()

name = input("Enter your name: ")
firstPerson["name"] = name
time.sleep(0)
os.system("clear")

dob = input("Enter your date of birth: ")
firstPerson["DoB"] = dob
time.sleep(0)
os.system("clear")

cell = input("Enter your cell number: ")
firstPerson["cell"] = cell
time.sleep(0)
os.system("clear")

email = input("Enter your email: ")
firstPerson["email"] = email
time.sleep(0)
os.system("clear")

address = input("Enter your address: ")
firstPerson["address"] = address
time.sleep(0)
os.system("clear")

print(f"Your name is: {firstPerson['name']}")
time.sleep(2)
os.system("clear")

print(f"Your date of birthday is: {firstPerson['DoB']}")
time.sleep(2)
os.system("clear")

print(f"Your cell number is: {firstPerson['cell']}")
time.sleep(2)
os.system("clear")

print(f"Your email is: {firstPerson['email']}")
time.sleep(2)
os.system("clear")

print(f"Your address is: {firstPerson['address']}")
time.sleep(2)
os.system("clear")


