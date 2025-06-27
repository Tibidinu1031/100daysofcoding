import csv 

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Cost"]) * float(row["Quantity"])

print(f"Total = {round(total, 2)}")