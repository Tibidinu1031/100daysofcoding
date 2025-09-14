print("Palindrome Checker")
print("----------")
print()


def palindrome(wordList):
    if len(wordList) <= 1:
        print("Palindrome")
        return
    elif wordList[0] == wordList[-1]:
        wordList.pop(0)
        wordList.pop(-1)
        print(wordList)
        palindrome(wordList)
    elif wordList[0] != wordList[-1]:
        print("Not a palindrome")
        return
    


while True:
    word = input("Enter a word:> ")
    wordList = list(word.lower())
    print(wordList)

    palindrome(wordList)
    print()
        
        

    