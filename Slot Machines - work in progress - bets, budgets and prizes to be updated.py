import random

print("Pacanele Time 7️⃣  7️⃣  7️⃣  7️⃣  7️⃣")
print("---------------------------")
print()

pacanea = ["7  ", "🍉", "🍋", "🍇", "🍒", "⭐", "🟣", "🍊"]

hand = []

cards = {"Rosie": ["♥️", "♦️"], "Neagra": ["♠️", "♣️"]}
cardsDealt = []

randomCard = random.choice(list(cards.values()))


def prettyPrint():
    print("--------------------------------------")
    for index in range(5):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")
    for index in range(5, 10):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")
    for index in range(10, 15):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")

budget = int(input("Insert Budget\n> "))
bet = int(input("Choose your bet\n> "))

while True:
    for i in range (0, 15):
        i = random.randint(0, len(pacanea) - 1)
        hand.append(pacanea[i])
        i += 1
        
    start = input("Press SPACE to start\n> ")
    budget -= bet
    prettyPrint()

    print(f"Remaining budget: {budget}")
    print(f"Bet: {bet}")
    print()

    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 10
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 10
                    print("Prize lost")
                    break
        else:
            bet *= 10
            print(f"Collected {bet}")
    elif hand[0] == hand[1] == hand[2] == hand[3]:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 5
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 5
                    print("Prize lost")
                    break
        else:
            bet *= 5
            print(f"Collected {bet}")
    elif hand[0] == hand[1] == hand[2]:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 3
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 3
                    print("Prize lost")
                    break
        else:
            bet *= 3
            print(f"Collected {bet}")


       
    if hand[5] == hand[6] == hand[7] == hand[8] == hand[9]:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 10
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 10
                    print("Prize lost")
                    break
        else:
            bet *= 10
            print(f"Collected {bet}")    
    elif hand[5] == hand[6] == hand[7] == hand[8]:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 5
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 5
                    print("Prize lost")
                    break
        else:
            bet *= 5
            print(f"Collected {bet}")
    elif hand[5] == hand[6] == hand[7]:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 3
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 3
                    print("Prize lost")
                    break
        else:
            bet *= 3
            print(f"Collected {bet}")


    if hand[10] == hand[11] == hand[12] == hand[13] == hand[14]:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 10
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 10
                    print("Prize lost")
                    break
        else:
            bet *= 10
            print(f"Collected {bet}")
    elif hand[10] == hand[11] == hand[12] == hand[13]:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 5
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 5
                    print("Prize lost")
                    break
        else:
            bet *= 5
            print(f"Collected {bet}")
    elif hand[10] == hand[11] == hand[12]:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 3
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 3
                    print("Prize lost")
                    break
        else:
            bet *= 3
            print(f"Collected {bet}")


    if hand[0] == hand[6] == hand[12] == hand[8] == hand[4]:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 10
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 10
                    print("Prize lost")
                    break
        else:
            bet *= 10
            print(f"Collected {bet}")
    elif hand[0] == hand[6] == hand[12] == hand[8]:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 5
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 5
                    print("Prize lost")
                    break
        else:
            bet *= 5
            print(f"Collected {bet}")
    elif hand[0] == hand[6] == hand[12]:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 3
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 3
                    print("Prize lost")
                    break
        else:
            bet *= 3
            print(f"Collected {bet}")


    if hand[10] == hand[6] == hand[2] == hand[8] == hand[14]:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 10
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 10
                    print("Prize lost")
                    break
        else:
            bet *= 10
            print(f"Collected {bet}")
    elif hand[10] == hand[6] == hand[2] == hand[8]:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 5
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 5
                    print("Prize lost")
                    break
        else:
            bet *= 5
            print(f"Collected {bet}")
    elif hand[10] == hand[6] == hand[2]:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            while True:
                index = 1
                prize = bet * 3
                print(f"Moara {index}")
                rosieNeagra = input("R. Rosie\nN. Neagra\n> ")
                randomCard = random.choice(list(cards.values()))
                print(randomCard)
                cardsDealt.append(randomCard)
                if rosieNeagra == randomCard:
                    prize *= 2
                    index += 1
                    if index >= 5:
                        break
                else:
                    prize = bet * 3
                    print("Prize lost")
                    break
        else:
            bet *= 3
            print(f"Collected {bet}")



    # special rules for cherries:
    if hand[0] == "🍒" or hand[5] == "🍒" or hand[10] == "🍒":
        if hand[0] == hand[1]:
            print("x2")
            doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 2

        if hand[5] == hand[6]:
            print("x2")
            doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 2

        if hand[10] == hand[11]:
            print("x2")
            doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 2

        if hand[0] == hand[6]:
            print("x2")
            doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 2

        if hand[10] == hand[6]:
            print("x2")
            doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 2
    # up until here

    # special rules for stars:
    if hand.count("⭐") == 3:
        print("x3")
        doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 3
    if hand.count("⭐") == 4:
        print("x4")
        doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 4
    if hand.count("⭐") == 5:
        print("x5")
        doubleDown = input("Try to double the prize or lose it all?\nD. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            print("Moara")
        else:
            bet *= 3
    # up until here

    hand = []

    


