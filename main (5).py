import random

numbers = []

for i in range(8):
  numbers.append(random.randint(1, 90))
numbers.sort()

my_2d_list = [ [numbers[0], numbers[1], numbers[2]],
               [numbers[3], "BINGO", numbers[4] ],
               [numbers[5], numbers[6], numbers[7]] ]

print(f"{my_2d_list[0][0]:^5} | {my_2d_list[0][1]:^5} | {my_2d_list[0][2]:^5}")
print("-------------------")
print(f"{my_2d_list[1][0]:^5} | {my_2d_list[1][1]:^5} | {my_2d_list[1][2]:^5}")
print("-------------------")
print(f"{my_2d_list[2][0]:^5} | {my_2d_list[2][1]:^5} | {my_2d_list[2][2]:^5}")