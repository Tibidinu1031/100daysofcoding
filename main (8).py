import os, time, random

print("Task Manager")
print()
list = []

fileExists = True
try:
  f = open("taskmanager.txt", "r")
  list = eval(f.read())
  f.close()
except:
  fileExists = False


def prettyPrint():
  for index in range(len(list)):
    print(f"{index+1}. {list[index]}")
  print()


while True:
  choice = input(
      "Kindly choose an option from the list below:\n 1. Add Task\n 2. View Tasks\n 3. Remove Task\n 4. Edit List\n 5. Clear\n 6. Exit\n --> "
  )
  if choice == "1":
    print()
    task = input("Kindly enter the task you want to add: ")
    if task in list:
      print()
      print(f"{task} is already in your list")
    else:
      print(f"{task} has been added to your list")
      list.append(task)
    prettyPrint()
  elif choice == "2":
    print()
    print("Your list is as follows:")
    prettyPrint()
    if len(list) == 0:
      print("=== empty list ===")
    print()
  elif choice == "3":
    print()
    task = input("Kindly enter the task you want to remove: ")
    confirmation = input(
        f"Are you sure you want to remove {task} from your list? (y/n) ")
    if confirmation == "y":
      if task in list:
        list.remove(task)
        print()
        print(f"{task} has been removed from your list")
        prettyPrint()
        if len(list) == 0:
          print("=== empty list ===")
          print()
          print()
      else:
        print()
        print(f"{task} is not in your list")
        prettyPrint()
        if len(list) == 0:
          print("=== empty list ===")
          print()
          print()
    elif confirmation == "n":
      print()
      print("No worries, the list remains unchanged, as shown below:")
      prettyPrint()
  if choice == "4":
    print()
    print("Your list is shown below:")
    prettyPrint()
    task = input("Kindly enter the number of the task you want to edit: ")
    dtask = int(task) - 1
    print(f"Task nr. {task} is {list[int(dtask)]}")
    new_task = input(f"Now what do you want to modify the {task} to: ")
    list[int(dtask)] = new_task
    print(f"Task nr. {task} has been changed to {new_task}")
    prettyPrint()

  if choice == "5":
    choice = input(
        "If you want to clear the task list - please choose 1\nIf you want to clear the screen - please choose 2\nIf you want to do both - please choose 3 \n--> "
    )
    if choice == "1":
      list.clear()
      print("Your list has been cleared")
    elif choice == "2":
      print("Your screen has been cleared")
      time.sleep(2)
      os.system("clear")

    elif choice == "3":
      print("Your screen and list have been cleared")
      list.clear()
      time.sleep(2)
      os.system("clear")

  if choice == "6":
    print("Execution time! See you later!")
    exit()

  if fileExists:
    try:
      os.mkdir("bah")
    except:
      pass
    name = "bah.txt"
    os.popen(f"cp taskmanager.txt bah/{name}")
    
  f = open("taskmanager.txt", "w")
  f.write(str(list))
  f.close()
