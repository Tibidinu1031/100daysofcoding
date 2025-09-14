print("Palindrome")
print("----------")
print()


while True:
    word = input("Enter a word:> ")
    wordList = list(word.lower())
    print(wordList)

    print()

    while True:
        if len(wordList) <= 1:
            print("Palindrome")
            break
        elif wordList[0] == wordList[-1]:
            wordList.pop(0)
            wordList.pop(-1)
            print(wordList)
        elif wordList[0] != wordList[-1]:
            print("Not a palindrome")
            break

    