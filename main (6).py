f = open("high.score", "r")

list = []

while True:
  contents = f.readline().strip()

  if contents == "":
    break

  contents = contents.split()
  list.append(contents)

  print(contents)

print()


if int(list[0][1]) > int(list[1][1]) and int(list[0][1]) > int(list[2][1]) and int(list[0][1]) > int(list[3][1]):
  print(f'{list[0][0]} is the highest score of {list[0][1]}')
elif int(list[1][1]) > int(list[0][1]) and int(list[1][1]) > int(list[2][1]) and int(list[1][1]) > int(list[3][1]):
  print(f'{list[1][0]} is the highest score of {list[1][1]}')
elif int(list[2][1]) > int(list[0][1]) and int(list[2][1]) > int(list[1][1]) and int(list[2][1]) > int(list[3][1]):
  print(f'{list[2][0]} is the highest score of {list[2][1]}')
elif int(list[3][1]) > int(list[0][1]) and int(list[3][1]) > int(list[1][1]) and int(list[3][1]) > int(list[2][1]):
  print(f'{list[3][0]} is the highest score of {list[3][1]}')

  






