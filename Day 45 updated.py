print("Advanced To Do List")
print()


todo_list = []


def prettyPrint():
  print()
  for row in todo_list:
    for item in row:
      print(f"{item:^10}", end = " | ")
    print()
  print()


def prettyPrintHigh():
  print()
  for row in todo_list:
    for item in row:
      if row[2] == "high":
        print(f"{item:^10}", end = " | ")
    print()
  print()


def prettyPrintLow():
  print()
  for row in todo_list:
    for item in row:
      if row[2] == "low":
        print(f"{item:^10}", end = " | ")
    print()
  print()


while True:
  choice = input("1. Add \n2. View \n3. Remove \n4. Edit \n5. Quit?\n \n>> ")
  if choice == "5":
    print("Goodbye!")
    break

  elif choice == "1":
    addChoice = input("What is it? >> ")
    dueDate = input("When is it due? >> ")
    priority = input("Is the priority high or low? >> ")
    print()
    row = [addChoice, dueDate, priority]
    todo_list.append(row)
    
  elif choice == "2":
    allHighLow = input("1. View all \n 2. View high priority tasks \n 3. View low priority tasks\n>> ")
    if allHighLow == "1":
      print("View the list")
      prettyPrint()
    elif allHighLow == "2":
      print("View the high priority list:")
      prettyPrintHigh()
    elif allHighLow == "3":    
      print("View the low priority list:")
      prettyPrintLow()
      
  elif choice == "3":
    choice = input("What task would you like to remove? >> ")
    for row in todo_list:
      for item in row:
        if item == choice:
          todo_list.remove(row)
          print(f"The {choice} task has been removed. Please check the remaining tasks below")
          if len(todo_list) > 0:
            prettyPrint()
          elif len(todo_list) == 0:
            print("There are no tasks left")
            
  elif choice == "4":
    editTo = input("What task would you like to edit? >> ")
    newEditTo = input("What would you like to change it to? >> ")
    dueDate = input("When is it due? >> ")
    priority = input("Is the priority high or low? >> ")
    for row in todo_list:
      if row[0] == editTo:
        row[0] = newEditTo
        row[1] = dueDate
        row[2] = priority
        
    prettyPrint()
    