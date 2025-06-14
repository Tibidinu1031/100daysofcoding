import random

while True:
  print("IDEAS")
  print("1. Add an Idea")
  print("2. Load a Random Idea")

  pick = input("> ")

  if pick == "1":
    idea = input("Idea: ") 
    f = open("my.ideaz", "a+")
    f.write(idea + "\n")
    f.flush()
    f.close()
  elif pick == "2":
    f = open("my.ideaz", "r")
    contents = f.read()
    contents = contents.split("\n")
    randomIdea = contents[random.randint(0, len(contents) - 2)]
    print(f"random idea: {randomIdea}")  
    f.close()
  