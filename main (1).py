print("Loan Calculator")
print()
loan = 1000
for counter in range(10):
  loan *= 1.05
  print(round(loan, 2))
print()
interestPaid = loan - 1000
print("You paid $", round(interestPaid, 2), "in interest!")
