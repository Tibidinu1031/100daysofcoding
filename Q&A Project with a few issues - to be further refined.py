import random, os

print("Flashcard Quiz")
print("--------------")

qnaDict = {}

fileExists = True
try:
  f = open("Q&As.txt", "r")
  orders = eval(f.read())
  f.close()
except:
  print()
  print("Welcome to:")
  fileExists = False

score = 0

while True:
    print("Menu")
    print("----")
    print()

    choice = input("1. Create a question and an answer for it.\n2. Practice the quiz with a random question\n> ")

    if choice == "1":
        key = input("Please state the question: ")
        value = input("Please state the answer: ")
        qnaDict[key] = value
        print(qnaDict)
    elif choice == "2":
        random_key = random.choice(list(qnaDict.keys()))
        print(random_key)
        userAnswer = input("Your answer: ")
        if userAnswer == qnaDict[random_key]:
            print("Correct")
            score += 1
            print(f"+1 to you. Your score is now {score}")
            print()
            if score >= 5:
                print("You won!")
                break
        else:
            print("Wrong")
            score -= 1
            print(f"-1 to you. Your score is now {score}")
            if score <= -5:
                print("You lost!")
                break
            print()

    if fileExists:
      try:
        os.mkdir("backup")
      except:
        pass
      backup_file = "Q&As.txt"
      os.system(f"cp 'Q&As.txt' backup/{backup_file}")

    f = open("Q&As.txt", "w")
    f.write(str(qnaDict))
    f.close()

    oneMoreTime = input("1. Let's do it again\n2. Exit\n> ")
    if oneMoreTime == "1":
        continue
    if oneMoreTime == "2":
        break