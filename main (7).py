
f = open("high.score", "r")

highscore = 0
name = None

while True:
  contents = f.readline()

  contents = contents.split()

  if contents == []:
    break
    
  if int(contents[1]) > highscore:
    highscore = int(contents[1])
    name = contents[0]
    print(highscore)
print(f"{name} has the highest score of {highscore}")

f.close()
  