import csv

print("Opening and Calculating data from CSV file programatically")
print("----------------------------------------------------------")
print()

grandTotal = 0

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Cost"])
        total = float(row["Cost"]) * int(row["Quantity"])
        grandTotal += total

print(round(grandTotal, 2))