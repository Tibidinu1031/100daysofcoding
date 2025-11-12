print()
print()
romanList = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

number = int(input("Enter a Normal number: "))

romanNumber = []

for key, value in romanList.items():
    count = number // key  
    if count:
        romanNumber.append(value * count)
        number -= key * count  

joinedRomanNumber = "".join(romanNumber)
print(f"Roman numeral: {joinedRomanNumber}")