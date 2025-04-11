print("Task Manager")
print()
list = []

def prettyPrint():
  for index in range(len(list)):
    print(f"{index+1}. {list[index]}")
  print()

while True:
  choice = input("Kindly choose an option from the list below:\n 1. Add Task\n 2. View Tasks\n 3. Remove Task\n 4. Edit List\n --> ")
  if choice == "1":
    print()
    task = input("Kindly enter the task you want to add: ")
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
    confirmation = input(f"Are you sure you want to remove {task} from your list? (y/n) ")
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
    new_task = input("Perfect, now kindly enter the new task: ")
    
    
