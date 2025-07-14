import os

print("Personal Expense Project")
print("------------------------")
print()

transactions = []
fileExists = True
try:
    f = open("expense.tracker", "r")
    transactions = eval(f.read())
    f.close()
except:
    print()
    print("If you are seeing this line it means that you have not made any transactions nor removed one so far.\n Once you do, it'll no longer show")
    print()
    fileExists = False

transactionNumber = 1
total = 0

def prettyPrint():
    print()
    print(f"{'Transaction #':^30} | {'Amount':^30} | {'Category':^30} | {'Note':^30} |")
    for rows in transactions:
        for items in rows:
            print(f"{str(items):^30}", end=" | ")
        print()
    print()

while True:
    pick = input("1. Add new transaction\n2. View the transactions so far\n3. View total\n> ")
    if pick == "1":
        print(f"Transaction number: {transactionNumber}")
        amount = input("What's the value of this transaction? > ")
        total += int(amount)
        category = input("What category does this transaction fall into? > ")
        addNote = input("Add a note?\nY/N\n> ")
        if addNote.lower() == "y":
            note = input("What are the details for this transaction? > ")
            print("Details added!")
            print()
            transactionLine = [transactionNumber, amount, category, note]
            transactions.append(transactionLine)
        else:
            note = "No Details"
            print("This transaction will have not details.")
            print()
            transactionLine = [transactionNumber, amount, category, note]
            transactions.append(transactionLine)
        prettyPrint()
        transactionNumber += 1
    if pick == "2":
        if transactions != []:
            prettyPrint()
            print()
        else:
            print("--- Empty list. Pleade log a transcation! ---")
            print()
    if pick == "3":
        print(f"Total Expenses = {total}$")
        print()


    f = open("expense.tracker", "w")
    f.write(str(transactions))
    f.close()
    
    if fileExists:
      try:
        os.mkdir("backup")
      except:
        pass
          
      backup_file = "expense.tracker"
      os.system(f"cp expense.tracker backup/{backup_file}")

    oneMore = input("Do you want to add another transaction?\nY/N\n> ")
    if oneMore.lower() == "n":
        print("Thank you for using this program!")
        break

    

