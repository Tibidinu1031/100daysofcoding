import os, time

print("MokeBeast")
print()
mokeMon = {"Beast Name" : None, "Type" : None, "Special Move " : None, "HP" : None, "MP" : None}

def mokeMonDesc():
  if mokeMon["Type"].lower() == "fire":
    print("\033[91m")
  elif mokeMon["Type"].lower() == "water":
    print("\033[94m")
  elif mokeMon["Type"].lower() == "earth":
    print("\033[92m")
  elif mokeMon["Type"].lower() == "air":
    print("\033[0m")
  elif mokeMon["Type"].lower() == "sky":
    print("\033[93m")
    
  print("===========================================")
  print()
  print(f"Beast Name: {mokeMon['Beast Name']}")
  print(f"Type: {mokeMon['Type']}")
  print(f"Special Move: {mokeMon['Special Move']}")
  print(f"HP: {mokeMon['HP']}")
  print(f"MP: {mokeMon['MP']}")
  print("\033[0m")

while True:
  beastName = input("Enter beast name: ")
  mokeMon["Beast Name"] = beastName
  
  type = input("Enter Type: ")
  mokeMon["Type"] = type
  
  special_move = input("Enter Special Move: ")
  mokeMon["Special Move"] = special_move
  
  hp = input("Enter HP: ")
  mokeMon["HP"] = hp
  
  mp = input("Enter MP: ")
  mokeMon["MP"] = mp
  
  mokeMonDesc()
  time.sleep(3)
  os.system("clear")
