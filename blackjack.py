import random

print("Welcome to the Blackjack Table")
print("------------------------------")
print()

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A"]

while True:
    start = input("Start> ")
    if start == "1":
        randomIndex1 = random.randint(1, len(cards) - 1)
        randomIndex2 = random.randint(1, len(cards) - 1)

        houseCard1 = cards[randomIndex1]
        houseCard1Value = 0

        houseCard2 = cards[randomIndex2]
        houseCard2Value = 0

        houseHand = houseCard1 + ", " + houseCard2
        houseHandTotal = 0

        randomIndex3 = random.randint(1, len(cards) - 1)
        randomIndex4 = random.randint(1, len(cards) - 1)

        playerCard1 = cards[randomIndex3]
        playerCard1Value = 0

        playerCard2 = cards[randomIndex4]
        playerCard2Value = 0

        playerHand = playerCard1 + ", " + playerCard2
        playerHandTotal = 0

        def houseHandTotal():
            if randomIndex1 >= 0 and randomIndex1 <= 9:
                houseCard1Value = int(cards[randomIndex1])
                print(f"Test: {houseCard1Value}")
            elif randomIndex1 == 10 or randomIndex1 == 11 or randomIndex1 == 12:
                houseCard1Value = 10
                print(f"Test: {houseCard1Value}")
            else:
                choice = input("You've been dealt an Ace as the first card.\n It can be used as either 1 or 11. Kindly insert the value below\n> ")
                if choice == "1":
                    houseCard1Value = 1
                    print(f"Test: {houseCard1Value}")
                else:
                    houseCard1Value = 11
                    print(f"Test: {houseCard1Value}")

            if randomIndex1 >= 0 and randomIndex2 <= 9:
                houseCard2Value = int(cards[randomIndex2])
                print(f"Test: {houseCard2Value}")
            elif randomIndex2 == 10 or randomIndex2 == 11 or randomIndex2 == 12:
                houseCard2Value = 10
                print(f"Test: {houseCard2Value}")
            else:
                choice = input("You've been dealt an Ace as the second card.\n It can be used as either 1 or 11. Kindly insert the value below\n> ")
                if choice == "1":
                    houseCard2Value = 1
                    print(f"Test: {houseCard2Value}")
                else:
                    houseCard2Value = 11
                    print(f"Test: {houseCard2Value}")

            houseHandTotal = houseCard1Value + houseCard2Value
            print(f"House's Hand: {houseCard1}, {houseCard2}")
            print(f"House's Total: {houseHandTotal}")

        def playerHandTotal():
            if randomIndex3 >= 0 and randomIndex3 <= 9:
                playerCard1Value = int(cards[randomIndex3])
                print(f"Test: {playerCard1Value}")
            elif randomIndex3 == 10 or randomIndex3 == 11 or randomIndex3 == 12:
                playerCard1Value = 10
                print(f"Test: {playerCard1Value}")
            else:
                choice = input("You've been dealt an Ace as the first card.\n It can be used as either 1 or 11. Kindly insert the value below\n> ")
                if choice == "1":
                    playerCard1Value = 1
                    print(f"Test: {playerCard1Value}")
                else:
                    playerCard1Value = 11
                    print(f"Test: {playerCard1Value}")

            if randomIndex4 >= 0 and randomIndex4 <= 9:
                playerCard2Value = int(cards[randomIndex4])
                print(f"Test: {playerCard2Value}")
            elif randomIndex4 == 10 or randomIndex4 == 11 or randomIndex4 == 12:
                playerCard2Value = 10
                print(f"Test: {playerCard2Value}")
            else:
                choice = input("You've been dealt an Ace as the second card.\n It can be used as either 1 or 11. Kindly insert the value below\n> ")
                if choice == "1":
                    playerCard2Value = 1
                    print(f"Test: {playerCard2Value}")
                else:
                    playerCard2Value = 11
                    print(f"Test: {playerCard2Value}")

            playerHandTotal = playerCard1Value + playerCard2Value
            print(f"House's Hand: {playerCard1}, {playerCard2}")
            print(f"House's Total: {playerHandTotal}")

        houseHandTotal()
        playerHandTotal()
        print()

  
