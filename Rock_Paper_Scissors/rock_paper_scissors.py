import tkinter as tk
from tkinter import messagebox
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Game logic
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play(player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{result}")

# GUI setup
frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Choose Rock, Paper or Scissors:", font=("Arial", 14))
label.pack(pady=10)

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
