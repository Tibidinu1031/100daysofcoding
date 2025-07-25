import random

print("Pacanele Time 7️⃣  7️⃣  7️⃣  7️⃣  7️⃣")
print("---------------------------")
print()

pacanea = ["7  ", "🍉", "🍋", "🍇", "🍒", "⭐", "🟣", "🍊"]

hand = []

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

while True:
    for i in range (0, 15):
        i = random.randint(0, len(pacanea) - 1)
        hand.append(pacanea[i])
        i += 1
        
    start = input("Press SPACE to start\n> ")
    prettyPrint()
    hand = []

    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        print("x10")
        
    if hand[5] == hand[6] == hand[7] == hand[8] == hand[9]:
        print("x10")
        
    if hand[10] == hand[11] == hand[12] == hand[13] == hand[14]:
        print("x10")
        
    if hand[0] == hand[1] == hand[2] == hand[3]:
        print("x5")
        
    if hand[5] == hand[6] == hand[7] == hand[8]:
        print("x5")
        
    if hand[10] == hand[11] == hand[12] == hand[13]:
        print("x5")
        
    if hand[0] == hand[1] == hand[2]:
        print("x3")
        
    if hand[5] == hand[6] == hand[7]:
        print("x3")
        
    if hand[10] == hand[11] == hand[12]:
        print("x3")


