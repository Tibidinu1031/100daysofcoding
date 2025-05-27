import os, time

print("MokeBeast")
print()
mokeMon = {}

def mokeMonDesc():
  if mokeMon[beastName]["Beast Type"].lower() == "fire":
    print("\033[91m")
  elif mokeMon[beastName]["Beast Type"].lower() == "water":
    print("\033[94m")
  elif mokeMon[beastName]["Beast Type"].lower() == "earth":
    print("\033[92m")
  elif mokeMon[beastName]["Beast Type"].lower() == "air":
    print("\033[0m")
  elif mokeMon[beastName]["Beast Type"].lower() == "sky":
    print("\033[93m")

  print("==============================================")
  print("The highlight for this pick is as shown below:")
  print(f"Beast Type        : {mokeMon[beastName]['Beast Type']}")
  print(f"HP                : {mokeMon[beastName]['HP']}")
  print(f"MP                : {mokeMon[beastName]['MP']}")
  print("==============================================")

  print("\033[0m")

  print()
  
  print("The table with all the picks is shown below:")

  print()
  
  print(f"{'Name':^14}", end=" | ")
  print(f"{'Type':^14}", end=" | ")
  print(f"{'HP':^14}", end=" | ")
  print(f"{'MP':^14}", end=" | ")
  print()
  for key, value in mokeMon.items():
    print(f"{key:^14}", end=' | ')
    for subkey, subvalue in value.items():
      print(f"{subvalue:^14}", end=' | ')
    print()


while True:
  print("")
  print("")
  beastName = input("Enter your beast name: ")

  beastType = input("Enter your beast type: ")

  hp = input("Enter your beast HP: ")

  mp = input("Enter your beast MP: ")

  mokeMon[beastName] = {"Beast Type" : beastType, "HP" : hp, "MP" : mp}
  
  mokeMonDesc()

  time.sleep(3)
  os.system("clear")

