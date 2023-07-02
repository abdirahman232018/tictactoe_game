import time

import tkinter as tk
from tkinter import messagebox
import random

# Function to handle button clicks
def button_click(row, col):
    global current_player  # This allows us to modify the global variable inside this function

    # Only proceed if the cell hasn't been filled yet
    if buttons[row][col]["text"] == "":
        # Fill the cell with the current player's symbol
        buttons[row][col]["text"] = current_player
        # Change the cell's color to yellow
        buttons[row][col]["bg"] = "yellow"

        window.update_idletasks()
        time.sleep(0.1)  # Pause for a moment to let the display update

        # Check if the current player has won
        if check_win(current_player):
            buttons[row][col]["text"] = current_player
            messagebox.showinfo("Game Over", f"{current_player} wins!")

            reset_game()
        # Check if the game is a tie
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # If the game isn't over, switch to the other player
            current_player = "O" if current_player == "X" else "X"
            # If the next player is the AI, make it take its turn
            if current_player == "O":
                ai_move()

# Function for the AI player to make a move
def ai_move():
    global current_player  # This allows us to modify the global variable inside this function

    # Find all the empty cells
    available_cells = []
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                available_cells.append((row, col))

    # Choose a random empty cell and fill it
    if len(available_cells) > 0:
        row, col = random.choice(available_cells)
        buttons[row][col]["text"] = current_player
        buttons[row][col]["bg"] = "yellow"  # Change the cell's color to yellow

        window.update_idletasks()
        time.sleep(0.1)  # Pause for a moment to let the display update

        # Check if the AI has won
        if check_win(current_player):
            buttons[row][col]["text"] = current_player
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            reset_game()
        # Check if the game is a tie
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # If the game isn't over, switch to the other player
            current_player = "X"



# Function to check for a win
def check_win(player):
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] == player:
            return True
    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] == player:
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

# Function to reset the game
def reset_game():
    global current_player

    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Set the board background color
board_color = "yellow"
window.configure(bg=board_color)

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=5,
                           command=lambda row=row, col=col: button_click(row, col), bg=board_color)
        button.grid(row=row, column=col, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)

# Set the initial player
current_player = "X"

# Run the main event loop
window.mainloop()

