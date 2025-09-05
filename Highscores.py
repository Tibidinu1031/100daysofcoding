print("Highscores with name initials, score, and save")
print()

while True:
    f = open("high.score", "a+")
    name = input("Enter your initials (3 letters): ")
    score = input("Enter your score: ")
    f.write(f"{name} ")
    f.write(f"{score}\n")
    f.close()
    addAnother = input("Add another? (Y/N)\n> ")
    if addAnother.lower() == 'y':
        continue
    else:
        break

