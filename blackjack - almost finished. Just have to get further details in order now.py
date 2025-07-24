import random, os, time

print("Welcome to the Blackjack Table")
print("------------------------------")
print()

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A"]

def houseHandTotall():
    global houseHandTotal
    houseHandTotal = 0
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

    if randomIndex2 >= 0 and randomIndex2 <= 9:
        houseCard2Value = int(cards[randomIndex2])

    elif randomIndex2 == 10 or randomIndex2 == 11 or randomIndex2 == 12:
        houseCard2Value = 10
        print(f"Test: {houseCard2Value}")
    else:
        houseCard2Value = 11
        houseCard2point1Value = houseCard2Value - 1
        print(f"Test: {houseCard2Value}/{houseCard2point1Value}")
# The below needs to be fixed
    if randomIndex1 != 13 and randomIndex2 != 13:
        houseHandTotal = houseCard1Value + houseCard2Value
        print(f"House's Hand: {houseCard1}, ? ")
        print(f"TEEEST::: House's Hand: {houseCard1}, {houseCard2}::::::::::::")
    else:
        houseHandTotal = houseCard1Value + houseCard2Value + houseCard2point1Value # especially this line
        print(f"House's Hand: {houseCard1}, ? ")
        print(f"TEEEST::: House's Hand: {houseCard1}, {houseCard2}::::::::::::")
#Until here
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
    global houseOneMoreRandomIndex
    if oneMoreRandomIndex >= 0 and oneMoreRandomIndex <= 9:
        oneMoreRandomIndexValue = int(cards[oneMoreRandomIndex])
        print(f"Test card: {cards[oneMoreRandomIndex]}")
    elif oneMoreRandomIndex == 10 or oneMoreRandomIndex == 11 or oneMoreRandomIndex == 12:
        oneMoreRandomIndexValue = 10
        print(f"Test card: {cards[oneMoreRandomIndex]}")
    else:
        if playerHandTotal <=21:
            oneMoreRandomIndexValue = 11
            print(f"Test card: {cards[oneMoreRandomIndex]}")
        else:
            oneMoreRandomIndexValue = 1
            print(f"Test card: {cards[oneMoreRandomIndex]}")
    playerHandTotal += oneMoreRandomIndexValue
    print(f"Player's Total: {playerHandTotal}")

def houseHandTotallAfterDraw():
    global houseHandTotal
    global houseOneMoreRandomIndex
    if houseOneMoreRandomIndex >= 0 and houseOneMoreRandomIndex <= 9:
        houseOneMoreRandomIndexValue = int(cards[houseOneMoreRandomIndex])
        print(f"Test card: {cards[houseOneMoreRandomIndex]}")
    elif houseOneMoreRandomIndex == 10 or houseOneMoreRandomIndex == 11 or houseOneMoreRandomIndex == 12:
        houseOneMoreRandomIndexValue = 10
        print(f"Test card: {cards[houseOneMoreRandomIndex]}")
    else:
        if houseHandTotal <=21:
            houseOneMoreRandomIndexValue = 11
            print(f"Test card: {cards[houseOneMoreRandomIndex]}")
        else:
            houseOneMoreRandomIndexValue = 1
            print(f"Test card: {cards[houseOneMoreRandomIndex]}")
    houseHandTotal += houseOneMoreRandomIndexValue
    print(f"House's Total: {houseHandTotal}")

while True:
    start = input("Start> ")
    if start == "1":
        randomIndex1 = random.randint(0, len(cards) - 1)
        randomIndex2 = random.randint(0, len(cards) - 1)

        houseCard1 = cards[randomIndex1]
        houseCard1Value = 0

        houseCard2 = cards[randomIndex2]
        

        houseHand = houseCard1 + ", " + houseCard2
        houseHandTotal = 0

        randomIndex3 = random.randint(0, len(cards) - 1)
        randomIndex4 = random.randint(0, len(cards) - 1)

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
            if playerHandTotal == 21:  # added this condition in order to automatically break if the player hits 21
                print("Blackjack/21.")
                break
            elif playerHandTotal <= 20:
                oneMoreCard = input("Draw another card?\n1. Yes\n2. No\n> ")
                if oneMoreCard == "1":
                    oneMoreRandomIndex = random.randint(0, len(cards) - 1)
                    oneMoreCard = cards[oneMoreRandomIndex]
                    print(f"You draw {oneMoreCard}")
                    print("----------------")
                    playerHandTotallAfterDraw()
                    print("----------------") 
                else:
                    print(f"You're staying with {playerHandTotal}")
                    break
            else:
                print("You crossed the 21 threshold and you are now busted. Better luck next time")
                print("House wins!")
                exit()
            
        
        while True:
            if houseHandTotal >= 17 and houseHandTotal <= 21:
                print(f"House stays with {houseHandTotal}")
                break
            elif houseHandTotal <= 16:
                houseOneMoreRandomIndex = random.randint(0, len(cards) - 1)
                houseOneMoreCard = cards[houseOneMoreRandomIndex]
                print(f"House draws an {houseOneMoreCard}")
                print("---------------------")
                houseHandTotallAfterDraw()
                print("---------------------")    
            else:
                print(f"House is busted with {houseHandTotal}")
                print("Player Wins")
                exit()
              
        if houseHandTotal > playerHandTotal:
            print("House wins!")
        elif houseHandTotal == playerHandTotal:
            print("That a draw!")
        else:
            print("Player wins!")

  #      time.sleep(3)
   #     os.system("cls")


  
