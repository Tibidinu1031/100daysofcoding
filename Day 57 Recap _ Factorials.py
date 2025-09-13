def factorial(plm):
    if plm == 1:
        return 1
    else:
        return plm * factorial(plm - 1)

print()
print(f"Factorial = {factorial(8)}")