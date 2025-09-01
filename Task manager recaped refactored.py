print("== Back To Coding == Task Manager")
print()

tasks = []
# tasks = [["task1", "due1", "high"], ["task2", "due2", "medium"], ["task3", "due3", "low"]]

def prettyPrint():
    for rows in tasks:
        for item in rows:
            print(f"{item:^15}", end="|")
        print()

def priorityPrint(priority):
    for rows in tasks:
        if priority in rows:
            for item in rows:
                print(f"{item:^15}", end="|")
            print()

while True:
    choice = input("1. Add\n2. View\n3. Remove\n4. Edit\n5. Exit\n> ")
    if choice == "1":
        task = input("What is it: ")
        due = input("When is it due: ")
        importance = input("How important is it (low, medium, high): ")
        choiceSet = [task, due, importance]
        tasks.append(choiceSet)
        print("Task added.")
        print()
    elif choice == "2":
        if tasks != []:
            allOrPriority = input("1. View all\n2. View by priority\n> ")
            if allOrPriority == "1":
                print("Tasks Listed below:")
                prettyPrint()
            if allOrPriority == "2":
                priority = input("What priority do you want to view (low, medium, high): ")
                if priority in ["high", "medium", "low"]:
                    print(f"{priority.capitalize()} Priority Tasks Listed below:")
                    priorityPrint(priority)
                else:
                    print("-- No tasks found with this priority --")
                    
            print()
        else:
            print("-- empty list --")
            print()
    elif choice == "3":
        removeItem = input("What item do you want to delete?\n> ")
        found = False
        for rows in tasks:
            if removeItem in rows:
                tasks.remove(rows)
                print("Task removed.")
                print()
                found = True
                break
        if not found:
            print("Task not found.")
            print()
    elif choice == "4":
        editItem = input("What item do you want to edit?\n> ")
        found = False
        for rows in tasks:
            if editItem in rows:
                task = input("What is it: ")
                due = input("When is it due: ")
                importance = input("How important is it (low, medium, high): ")
                choiceSet = [task, due, importance]
                tasks[tasks.index(rows)] = choiceSet
                print("Task edited.")
                print()
                found = True
                break
        if not found:
            print("Task not found.")
            print()
    elif choice == "5":
        print("Ciao")
        break