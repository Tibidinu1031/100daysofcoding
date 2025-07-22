import random

print("Welcome to the Blackjack Table")
print("------------------------------")
print()

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A"]

def houseHandTotall():
    global houseCard2Value
    houseCard2Value = 0
    if randomIndex1 >= 0 and randomIndex1 <= 9:
        houseCard1Value = int(cards[randomIndex1])
        print(f"Test: {houseCard1Value}")
    elif randomIndex1 == 10 or randomIndex1 == 11 or randomIndex1 == 12:
        houseCard1Value = 10
        print(f"Test: {houseCard1Value}")
    else:
        if houseHandTotal <=21:
            houseCard1Value = 11
            print(f"Test: {houseCard1Value}")
        else:
            houseCard1Value = 1
            print(f"Test: {houseCard1Value}")

    if randomIndex1 >= 0 and randomIndex2 <= 9:
        houseCard2Value = int(cards[randomIndex2])
        print(f"Test: {houseCard2Value}")
    elif randomIndex2 == 10 or randomIndex2 == 11 or randomIndex2 == 12:
        houseCard2Value = 10
        print(f"Test: {houseCard2Value}")
    else:
        if houseHandTotal <=21:
            houseCard2Value = 11
            print(f"Test: {houseCard2Value}")
        else:
            houseCard2Value = 1
            print(f"Test: {houseCard2Value}")

    houseHandTotal = houseCard1Value + houseCard2Value
    print(f"House's Hand: {houseCard1}, {houseCard2}")
    print(f"House's Total: {houseHandTotal}")

def playerHandTotall():
    global playerHandTotal
    playerHandTotal = 0
    if randomIndex3 >= 0 and randomIndex3 <= 9:
        playerCard1Value = int(cards[randomIndex3])
        print(f"Test: {playerCard1Value}")
    elif randomIndex3 == 10 or randomIndex3 == 11 or randomIndex3 == 12:
        playerCard1Value = 10
        print(f"Test: {playerCard1Value}")
    else:
        if playerHandTotal <=21:
            playerCard1Value = 11
            print(f"Test: {playerCard1Value}")
        else:
            playerCard1Value = 1
            print(f"Test: {playerCard1Value}")

    if randomIndex4 >= 0 and randomIndex4 <= 9:
        playerCard2Value = int(cards[randomIndex4])
        print(f"Test: {playerCard2Value}")
    elif randomIndex4 == 10 or randomIndex4 == 11 or randomIndex4 == 12:
        playerCard2Value = 10
        print(f"Test: {playerCard2Value}")
    else:
        if playerHandTotal <=21:
            playerCard2Value = 11
            print(f"Test: {playerCard2Value}")
        else:
            playerCard2Value = 1
            print(f"Test: {playerCard2Value}")

    playerHandTotal = playerCard1Value + playerCard2Value
    print(f"Player's Hand: {playerCard1}, {playerCard2}")
    print(f"Player's Total: {playerHandTotal}")

def playerHandTotallAfterDraw():
    global playerHandTotal
    global oneMoreRandomIndex
    if oneMoreRandomIndex >= 0 and oneMoreRandomIndex <= 9:
        oneMoreRandomIndexValue = int(cards[oneMoreRandomIndex])
        print(f"Test: {oneMoreRandomIndex}")
    elif oneMoreRandomIndex == 10 or oneMoreRandomIndex == 11 or oneMoreRandomIndex == 12:
        oneMoreRandomIndexValue = 10
        print(f"Test: {oneMoreRandomIndex}")
    else:
        if playerHandTotal <=21:
            oneMoreRandomIndexValue = 11
            print(f"Test: {oneMoreRandomIndexValue}")
        else:
            oneMoreRandomIndexValue = 1
            print(f"Test: {oneMoreRandomIndexValue}")
    playerHandTotal += oneMoreRandomIndexValue
    #Have to move
    #The conditional for < 21 
    # Here
    # !!!!
    # Not finished, but good progress so far
    print(f"Player's Total: {playerHandTotal}")

while True:
    start = input("Start> ")
    if start == "1":
        randomIndex1 = random.randint(1, len(cards) - 1)
        randomIndex2 = random.randint(1, len(cards) - 1)

        houseCard1 = cards[randomIndex1]
        houseCard1Value = 0

        houseCard2 = cards[randomIndex2]
        

        houseHand = houseCard1 + ", " + houseCard2
        houseHandTotal = 0

        randomIndex3 = random.randint(1, len(cards) - 1)
        randomIndex4 = random.randint(1, len(cards) - 1)

        playerCard1 = cards[randomIndex3]
        playerCard1Value = 0

        playerCard2 = cards[randomIndex4]
        playerCard2Value = 0

        playerHand = playerCard1 + ", " + playerCard2

        print("----------------")
        houseHandTotall()
        print()
        playerHandTotall()
        print("----------------")  
        
        while True:
            oneMoreCard = input("Draw another card?\n1. Yes\n2. No\n> ")
            if oneMoreCard == "1":
                if playerHandTotal < 21:
                    oneMoreRandomIndex = random.randint(1, len(cards) - 1)
                    oneMoreCard = cards[oneMoreRandomIndex]
                    print(f"You draw {oneMoreCard}")
                    print("----------------")
                    playerHandTotallAfterDraw()
                    print("----------------") 
                else:
                    print("You crossed the 21 threshold and you are now busted. Better luck next time")
                    exit()
            else:
                print("//////TEEEEMP CONGRATS////////")
                break


  
