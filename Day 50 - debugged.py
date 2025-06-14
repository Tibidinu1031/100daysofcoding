import random, os, time

while True:
  print("IDEAS")
  print("1. Add an Idea")
  print("2. Load a Random Idea")

  pick = input("> ")

  if pick == "1":
    idea = input("Idea: ") 
    f = open("my.ideaz", "a+")
    f.write(f"{idea}\n")
    f.flush()
    f.close()
    time.sleep(1)
    os.system("cls")
  elif pick == "2":
    f = open("my.ideaz", "r")
    contents = f.read()
    if contents == "":
      print("Empty file. Please add an idea.")
      continue
    contents = contents.split("\n")
    contents.remove("")
    print(contents)
    randomIndex = random.randint(0, len(contents) - 1)
    print(f"Debug: random index: {randomIndex}")
    randomIdea = contents[randomIndex]
    print(f"Debug: random idea is: {randomIdea}")
    print(f"random idea: {randomIdea}") 
    time.sleep(1)
    os.system("cls") 
    f.close()
  