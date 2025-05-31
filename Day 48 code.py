f = open("highscore.txt", "a+")

import random
volta = 0

while True:
  user = input("Enter your username: ")
  score = random.randint(1, 100000)
  volta += 1
  print()
  f.write(f"{user} {score}\n")
  f.flush()
  if volta == 4:
    f.write("\n")
    f.close()
    break
