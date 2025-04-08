toDoListManager = []

def colorChanger(color):
  if color == "green":
    return "\033[32m"
  if color == "reset":
    return "\033[0m"

print(f"{colorChanger('green')}To Do List Manager {colorChanger('reset')}")
print()



def printList():
  print()
  if not toDoListManager:
    print("-- Empty list. Please add a task. --")
  else:
    for i in toDoListManager:
      print(i)
  print()

while True:
  choice = input("Enter add, remove, view or quit: ")
  if choice == "quit":
    print("Thank you for using the To Do List Manager.")
    break
  if choice == "add":
    task = input("Enter task: ")
    toDoListManager.append(task)
    print(f"{task} has been added to the list.")
  elif choice == "remove":
    task = input("Which item have you completed and now needs to be removed?: ")
    print(f"{task} has been removed from the list.")
    print("Remaining tasks: ")
    if task in toDoListManager:  
      toDoListManager.remove(task)
    else:
      print(f"{task} is not in the list.")    
  elif choice == "view":
    print("Showing the list:")
    if toDoListManager == []:
      print("Empty list. Please add a task.")
  printList()

  