import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from threading import Thread

class SlotMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Slot Machine 🎰")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a2e')
        
        # Game variables
        self.symbols = ["7️⃣", "🍉", "🍋", "🍇", "🍒", "⭐", "🟣", "🍊"]
        self.hand = []
        self.budget = 0
        self.bet = 0
        self.spinning = False
        
        # Card game variables
        self.cards = {"Rosie": ["♥️", "♦️"], "Neagra": ["♠️", "♣️"]}
        self.cards_dealt = []
        
        self.setup_ui()
        self.setup_game()
    
    def setup_ui(self):
        # Title
        title_frame = tk.Frame(self.root, bg='#1a1a2e')
        title_frame.pack(pady=10)
        
        title_label = tk.Label(title_frame, text="🎰 SLOT MACHINE 🎰", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ffd700', bg='#1a1a2e')
        title_label.pack()
        
        # Budget and Bet Frame
        control_frame = tk.Frame(self.root, bg='#1a1a2e')
        control_frame.pack(pady=10)
        
        tk.Label(control_frame, text="Budget:", font=('Arial', 12, 'bold'), 
                fg='white', bg='#1a1a2e').grid(row=0, column=0, padx=5)
        self.budget_entry = tk.Entry(control_frame, font=('Arial', 12), width=10)
        self.budget_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(control_frame, text="Bet:", font=('Arial', 12, 'bold'), 
                fg='white', bg='#1a1a2e').grid(row=0, column=2, padx=5)
        self.bet_entry = tk.Entry(control_frame, font=('Arial', 12), width=10)
        self.bet_entry.grid(row=0, column=3, padx=5)
        
        self.set_budget_btn = tk.Button(control_frame, text="Set Budget & Bet", 
                                       command=self.set_budget_bet,
                                       font=('Arial', 10, 'bold'),
                                       bg='#4CAF50', fg='white')
        self.set_budget_btn.grid(row=0, column=4, padx=10)
        
        # Display current budget and bet
        self.info_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.info_frame.pack(pady=5)
        
        self.budget_label = tk.Label(self.info_frame, text="Budget: $0", 
                                    font=('Arial', 14, 'bold'), 
                                    fg='#00ff00', bg='#1a1a2e')
        self.budget_label.pack(side=tk.LEFT, padx=20)
        
        self.bet_label = tk.Label(self.info_frame, text="Bet: $0", 
                                 font=('Arial', 14, 'bold'), 
                                 fg='#ffff00', bg='#1a1a2e')
        self.bet_label.pack(side=tk.RIGHT, padx=20)
        
        # Slot Machine Grid
        self.slot_frame = tk.Frame(self.root, bg='#2d2d44', relief=tk.RAISED, bd=5)
        self.slot_frame.pack(pady=20)
        
        self.slot_labels = []
        for row in range(3):
            row_labels = []
            for col in range(5):
                label = tk.Label(self.slot_frame, text="🎰", 
                               font=('Arial', 32), 
                               width=3, height=1,
                               bg='white', relief=tk.SUNKEN, bd=2)
                label.grid(row=row, column=col, padx=2, pady=2)
                row_labels.append(label)
            self.slot_labels.append(row_labels)
        
        # Spin Button
        self.spin_btn = tk.Button(self.root, text="🎰 SPIN 🎰", 
                                 command=self.spin_slots,
                                 font=('Arial', 18, 'bold'),
                                 bg='#ff4444', fg='white',
                                 width=15, height=2,
                                 state=tk.DISABLED)
        self.spin_btn.pack(pady=20)
        
        # Result Display
        self.result_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.result_frame.pack(pady=10)
        
        self.result_label = tk.Label(self.result_frame, text="", 
                                    font=('Arial', 16, 'bold'), 
                                    fg='#ffd700', bg='#1a1a2e')
        self.result_label.pack()
        
        # Double Down Frame (initially hidden)
        self.double_down_frame = tk.Frame(self.root, bg='#1a1a2e')
        
        tk.Label(self.double_down_frame, text="Double Down Mini-Game!", 
                font=('Arial', 14, 'bold'), fg='#ffd700', bg='#1a1a2e').pack()
        
        self.card_info_label = tk.Label(self.double_down_frame, text="", 
                                       font=('Arial', 12), fg='white', bg='#1a1a2e')
        self.card_info_label.pack(pady=5)
        
        card_btn_frame = tk.Frame(self.double_down_frame, bg='#1a1a2e')
        card_btn_frame.pack(pady=5)
        
        self.rosie_btn = tk.Button(card_btn_frame, text="♥️ Rosie ♦️", 
                                  command=lambda: self.play_card_game("Rosie"),
                                  font=('Arial', 12, 'bold'),
                                  bg='#ff6b6b', fg='white')
        self.rosie_btn.pack(side=tk.LEFT, padx=10)
        
        self.neagra_btn = tk.Button(card_btn_frame, text="♠️ Neagra ♣️", 
                                   command=lambda: self.play_card_game("Neagra"),
                                   font=('Arial', 12, 'bold'),
                                   bg='#333333', fg='white')
        self.neagra_btn.pack(side=tk.LEFT, padx=10)
        
        self.collect_btn = tk.Button(self.double_down_frame, text="💰 Collect Prize 💰", 
                                    command=self.collect_prize,
                                    font=('Arial', 12, 'bold'),
                                    bg='#4CAF50', fg='white')
        self.collect_btn.pack(pady=10)
    
    def setup_game(self):
        # Initialize empty grid
        for row in range(3):
            for col in range(5):
                self.slot_labels[row][col].config(text="🎰")
    
    def set_budget_bet(self):
        try:
            budget = int(self.budget_entry.get())
            bet = int(self.bet_entry.get())
            
            if budget <= 0 or bet <= 0:
                messagebox.showerror("Error", "Budget and bet must be positive numbers!")
                return
            
            if bet > budget:
                messagebox.showerror("Error", "Bet cannot be higher than budget!")
                return
            
            self.budget = budget
            self.bet = bet
            self.update_display()
            self.spin_btn.config(state=tk.NORMAL)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def update_display(self):
        self.budget_label.config(text=f"Budget: ${self.budget}")
        self.bet_label.config(text=f"Bet: ${self.bet}")
    
    def spin_slots(self):
        if self.spinning:
            return
        
        if self.budget < self.bet:
            messagebox.showwarning("Insufficient Funds", "Not enough budget to place bet!")
            return
        
        self.spinning = True
        self.spin_btn.config(state=tk.DISABLED, text="SPINNING...")
        self.result_label.config(text="")
        self.hide_double_down()
        
        # Deduct bet
        self.budget -= self.bet
        self.update_display()
        
        # Start spinning animation
        Thread(target=self.animate_spin, daemon=True).start()
    
    def animate_spin(self):
        # Spinning animation
        for _ in range(20):  # 20 frames of animation
            self.hand = []
            for i in range(15):
                symbol = random.choice(self.symbols)
                self.hand.append(symbol)
            
            # Update display
            self.root.after(0, self.update_slot_display)
            time.sleep(0.1)
        
        # Final result
        self.hand = []
        for i in range(15):
            symbol = random.choice(self.symbols)
            self.hand.append(symbol)
        
        self.root.after(0, self.finish_spin)
    
    def update_slot_display(self):
        for row in range(3):
            for col in range(5):
                index = row * 5 + col
                self.slot_labels[row][col].config(text=self.hand[index])
    
    def finish_spin(self):
        self.update_slot_display()
        self.spinning = False
        self.spin_btn.config(state=tk.NORMAL, text="🎰 SPIN 🎰")
        
        # Check for wins
        self.check_wins()
    
    def check_wins(self):
        win_multiplier = 0
        win_message = ""
        
        # Check horizontal lines (rows)
        # Top row (0-4)
        if self.hand[0] == self.hand[1] == self.hand[2] == self.hand[3] == self.hand[4]:
            win_multiplier = 10
            win_message = "TOP ROW - 5 IN A ROW!"
        elif self.hand[0] == self.hand[1] == self.hand[2] == self.hand[3]:
            win_multiplier = 5
            win_message = "TOP ROW - 4 IN A ROW!"
        elif self.hand[0] == self.hand[1] == self.hand[2]:
            win_multiplier = 3
            win_message = "TOP ROW - 3 IN A ROW!"
        
        # Middle row (5-9)
        elif self.hand[5] == self.hand[6] == self.hand[7] == self.hand[8] == self.hand[9]:
            win_multiplier = 10
            win_message = "MIDDLE ROW - 5 IN A ROW!"
        elif self.hand[5] == self.hand[6] == self.hand[7] == self.hand[8]:
            win_multiplier = 5
            win_message = "MIDDLE ROW - 4 IN A ROW!"
        elif self.hand[5] == self.hand[6] == self.hand[7]:
            win_multiplier = 3
            win_message = "MIDDLE ROW - 3 IN A ROW!"
        
        # Bottom row (10-14)
        elif self.hand[10] == self.hand[11] == self.hand[12] == self.hand[13] == self.hand[14]:
            win_multiplier = 10
            win_message = "BOTTOM ROW - 5 IN A ROW!"
        elif self.hand[10] == self.hand[11] == self.hand[12] == self.hand[13]:
            win_multiplier = 5
            win_message = "BOTTOM ROW - 4 IN A ROW!"
        elif self.hand[10] == self.hand[11] == self.hand[12]:
            win_multiplier = 3
            win_message = "BOTTOM ROW - 3 IN A ROW!"
        
        # Check diagonals
        elif self.hand[0] == self.hand[6] == self.hand[12] == self.hand[8] == self.hand[14]:
            win_multiplier = 10
            win_message = "DIAGONAL - 5 IN A ROW!"
        elif self.hand[0] == self.hand[6] == self.hand[12] == self.hand[8]:
            win_multiplier = 5
            win_message = "DIAGONAL - 4 IN A ROW!"
        elif self.hand[0] == self.hand[6] == self.hand[12]:
            win_multiplier = 3
            win_message = "DIAGONAL - 3 IN A ROW!"
        
        elif self.hand[10] == self.hand[6] == self.hand[2] == self.hand[8] == self.hand[14]:
            win_multiplier = 10
            win_message = "DIAGONAL - 5 IN A ROW!"
        elif self.hand[10] == self.hand[6] == self.hand[2] == self.hand[8]:
            win_multiplier = 5
            win_message = "DIAGONAL - 4 IN A ROW!"
        elif self.hand[10] == self.hand[6] == self.hand[2]:
            win_multiplier = 3
            win_message = "DIAGONAL - 3 IN A ROW!"
        
        # Check for cherries
        elif "🍒" in [self.hand[0], self.hand[5], self.hand[10]]:
            if self.hand[0] == self.hand[1]:
                win_multiplier = 2
                win_message = "CHERRY BONUS!"
        
        # Check for stars
        star_count = self.hand.count("⭐")
        if star_count >= 5:
            win_multiplier = 5
            win_message = f"STAR BONUS - {star_count} STARS!"
        elif star_count >= 4:
            win_multiplier = 4
            win_message = f"STAR BONUS - {star_count} STARS!"
        elif star_count >= 3:
            win_multiplier = 3
            win_message = f"STAR BONUS - {star_count} STARS!"
        
        if win_multiplier > 0:
            self.current_prize = self.bet * win_multiplier
            self.result_label.config(text=f"🎉 {win_message} 🎉\nPrize: ${self.current_prize} (x{win_multiplier})")
            self.show_double_down()
        else:
            self.result_label.config(text="No win this time. Try again!")
    
    def show_double_down(self):
        self.double_down_frame.pack(pady=10)
        self.update_card_display()
    
    def hide_double_down(self):
        self.double_down_frame.pack_forget()
    
    def update_card_display(self):
        if len(self.cards_dealt) == 0:
            self.card_info_label.config(text="No cards have been picked yet")
        elif len(self.cards_dealt) == 1:
            self.card_info_label.config(text=f"Last card: {self.cards_dealt[-1]}")
        elif len(self.cards_dealt) == 2:
            self.card_info_label.config(text=f"Last cards: {self.cards_dealt[-2]} {self.cards_dealt[-1]}")
        else:
            self.card_info_label.config(text=f"Last cards: {self.cards_dealt[-3]} {self.cards_dealt[-2]} {self.cards_dealt[-1]}")
    
    def play_card_game(self, choice):
        random_card = random.choice(list(self.cards.keys()))
        self.cards_dealt.append(random_card)
        
        if choice == random_card:
            self.current_prize *= 2
            self.result_label.config(text=f"🎉 CORRECT! Prize doubled to ${self.current_prize}! 🎉\nGuess again or collect!")
            self.update_card_display()
        else:
            self.result_label.config(text=f"❌ Wrong! The card was {random_card}. Prize lost!")
            self.hide_double_down()
    
    def collect_prize(self):
        self.budget += self.current_prize
        self.update_display()
        self.result_label.config(text=f"💰 Collected ${self.current_prize}! 💰")
        self.hide_double_down()

def main():
    root = tk.Tk()
    game = SlotMachineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
