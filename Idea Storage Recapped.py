import random

print("Idea Storage - Recap")
print()


while True:
    choice = input("1. Add new idea\n2. Display random idea\n3. Exit\n> ")
    if choice == "1":
        f = open("my.ideas", "a+")
        addIdea = input("Enter your brilliant idea:> ")
        f.write(f"{addIdea}\n")
        print(f"{addIdea} has been added to your idea list.")
        print()
        f.close()
    if choice == "2":
        f = open("my.ideas", "r")
        ideas = f.readlines()
        if ideas == []:
            print("No ideas stored yet.")
            print()
        else:
            randomIdea = random.choice(ideas)
            print(f"Here's a random idea: {randomIdea}")
            print()
    elif choice == "3":
        print("Goodbye!")
        break

