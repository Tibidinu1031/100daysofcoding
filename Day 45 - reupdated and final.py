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
    print(f"The {addChoice} task has been added to the list.")
    prettyPrint()
    
  elif choice == "2":
    allHighLow = input("1. View all \n 2. View high priority tasks \n 3. View low priority tasks\n>> ")
    if allHighLow == "1":
      print("View the list:")
      prettyPrint()
      if len(todo_list) == 0:
        print(" --- empty list --- ")
        print()
    elif allHighLow == "2":
      print("View the high priority list:")
      prettyPrintHigh()
      if len(todo_list) == 0:
        print(" --- empty list --- ")
        print()
    elif allHighLow == "3":    
      print("View the low priority list:")
      prettyPrintLow()
      if len(todo_list) == 0:
        print(" --- empty list --- ")
        print()
      
  elif choice == "3":
    removeItem = input("What task would you like to remove? >> ")
    found = False
    for row in todo_list:
      if row[0] == removeItem:
        found = True
        todo_list.remove(row)
        print(f"The {removeItem} has been removed.")
        if len(todo_list) >= 1:
          prettyPrint()
        else:
          print("The remaining tasks are shown below")
          print("--- empty list ---")
          print()

    if not found:
      print("There is not task with this name. Please check the To-Do List below:")
      prettyPrint()
      if len(todo_list) == 0:
        print(" --- empty list --- ")
        print()
            
  elif choice == "4":
    edit = input("What task do you want to edit? >> ")
    found = False
    for row in todo_list:
      if row[0] == edit:
        newEdit = input(f"What do you want {edit} to be modified to? >> ")
        dueDate = input(f"What's the due date for the {newEdit} task? >>")
        priority = input("What's the priority?")
        row[0] = newEdit
        row[1] = dueDate
        row[2] = priority
        found = True
        print(f"{edit} has been modified to {newEdit}")
        prettyPrint()
  
    if not found:
      print("There is no such task in the To-Do List. Please see the tasks below:")
      prettyPrint()
      if len(todo_list) == 0:
        print(" --- empty list --- ")
        print()
    