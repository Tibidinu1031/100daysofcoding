print()
print()
romanList = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

number = input("Enter a Normal number: ")

list_number = list(number)
print(list_number)
romanNumber = []
joinedRomanNumber = "".join(romanNumber)

for items in range(len(list_number)):
    romanNumber.append(romanList[int(list_number[items])])
print(romanNumber)