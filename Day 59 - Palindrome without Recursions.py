import os, time

print("Palindrome Checker")
print()

while True:
    word = input("Please choose a word ==> ")

    word2 = word[::-1]

    print(f"Word1: {word} | Word2: {word2}")

    if word == word2:
        print("Palindrome!!!")
    else:
        print("Not a Palindrome!")

    time.sleep(3)
    os.system("cls")
    

