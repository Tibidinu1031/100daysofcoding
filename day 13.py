print("Exam Day Calculator")
print()
nameOfExam = "Neuroscience"
print("Name of Exam: ", nameOfExam)
print()
maxScore = 100
print("Max. Possible Score: ", maxScore)
print()
yourScore = int(input("You exam score is: "))
scorePercentage = float(yourScore / maxScore) * 100
if scorePercentage >= 0 and scorePercentage <= 49:
  print("You got ", scorePercentage, "%.", "That is a U")
elif scorePercentage >= 50 and scorePercentage <= 59:
  print("You got ", scorePercentage, "%.", "That is a D")
elif scorePercentage >= 60 and scorePercentage <= 69:
  print("You got ", scorePercentage, "%.", "That is a C")
elif scorePercentage >= 70 and scorePercentage <= 79:
  print("You got ", scorePercentage, "%.", "That is a B")
elif scorePercentage >= 80 and scorePercentage <= 89:
  print("You got ", scorePercentage, "%.", "That is an A-")
elif scorePercentage >= 90 and scorePercentage <= 100:
  print("You got ", scorePercentage, "%.", "That is an A+")
else:
  print("Probably you have to assess the grade again!")

