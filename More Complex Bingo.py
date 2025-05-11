import random


numbers = []


while len(numbers) < 8:
  num = random.randint(1, 90)
  if num not in numbers:
    numbers.append(num)


numbers.sort()


def prettyPrint():
  print()
  print(f"{numbers[0]:^5} | {numbers[1]:^5} | {numbers[2]:^5}")
  print("-------------------")
  print(f"{numbers[3]:^5} | {my_2d_list[1][1]:^5} | {numbers[4]:^5}")
  print("-------------------")
  print(f"{numbers[5]:^5} | {numbers[6]:^5} | {numbers[7]:^5}")
  print()
  

my_2d_list = [[numbers[0], numbers[1], numbers[2]],
              [numbers[3], "BINGO", numbers[4]],
              [numbers[5], numbers[6], numbers[7]]]


print("Initial Bingo Card:")
print()
prettyPrint()
#print(f"{my_2d_list[0][0]:^5} | {my_2d_list[0][1]:^5} | {my_2d_list[0][2]:^5}")
#print("-------------------")
#print(f"{my_2d_list[1][0]:^5} | {my_2d_list[1][1]:^5} | {my_2d_list[1][2]:^5}")
#print("-------------------")
#print(f"{my_2d_list[2][0]:^5} | {my_2d_list[2][1]:^5} | {my_2d_list[2][2]:^5}")

while True:
  userChoice = input("What number comes up next? >> ")
  for i in range(len(numbers)):
    if numbers[i] == int(userChoice):
      print(f"{numbers[i]} has been marked with an X on your BINGO card.")
      numbers[i] = "x"
      print(numbers[i])
  if numbers[0] == "x" and numbers[1] == "x" and numbers[2] == "x" and numbers[3] == "x" and numbers[4] == "x" and numbers[5] == "x" and numbers[6] == "x" and numbers[7] == "x":
    print("Ding Ding Ding - You've hit the BINGO!")
    break
    
  print()    
  prettyPrint()
