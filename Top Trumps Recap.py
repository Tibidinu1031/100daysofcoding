import random

print("Top Trumps Recapped")
print()

rafaNadal = {"AO": 2, "RG": 14, "WB": 2, "USO": 4}
rogerFederer = {"AO": 6, "RG": 1, "WB": 8, "USO": 5}
djokerNole = {"AO": 10, "RG": 3, "WB": 7, "USO": 4}

goatStats = {"Rafa Nadal": rafaNadal, "Roger Federer": rogerFederer, "Novak Djokovic": djokerNole}

print("Tennis GOATs:")
for key in goatStats: 
    print(key)
print()

round = 1

while True:
    choice = input("Press 's' to start a round or 'q' to quit\n> ").lower()
    print(f"Round {round}")
    print()

    if choice == "s":
    
        player1Choice = random.choice(list(goatStats.keys()))
        print(f"Player 1 has chosen {player1Choice}")

        player2Choice = random.choice(list(goatStats.keys()))
        print(f"Player 2 has chosen {player2Choice}")

        slam = random.choice(["AO", "RG", "WB", "USO"]).upper()

        if player1Choice != player2Choice:
            if goatStats[player1Choice][slam] > goatStats[player2Choice][slam]:
                print(f"{player1Choice} has more {slam} slams!. Player 1 wins!")
                print()
            elif goatStats[player1Choice][slam] < goatStats[player2Choice][slam]:
                print(f"{player2Choice} has more {slam} slams! Player 2 wins!")  
                print()  
            else:
                print(f"{player1Choice} has as many {slam}s as {player2Choice}. It's a draw!")
                print()
        else:
            print("Both players chose the same GOAT, it's a draw!")

    if choice == "q":
        print("Thanks for playing!")
        break

        
