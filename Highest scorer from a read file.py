print("Highest Scorer from a read file")
print()

highestScore = 0

f = open("high.score", "r")

while True:  
    contents = f.readline().strip()
    splittedContents = contents.split()
    print(contents) 
    if contents == "":
        break
    if int(splittedContents[1]) > highestScore:
        highestScore = int(splittedContents[1])
        highestScorer = splittedContents[0]
    print(f"{highestScorer} has the highest score of {highestScore}")

f.close()