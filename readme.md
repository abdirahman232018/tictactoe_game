# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game implemented in Python using the Tkinter library for the graphical user interface. The game can be played by one player against an AI opponent. The AI makes its move randomly among the available cells.

## Features

- Graphical user interface created using Tkinter.
- AI opponent that randomly selects an empty cell for its move.
- Game board cells change color to yellow when filled.
- Checks for win or tie conditions after every move.
- Alert messages for game over scenarios: win or tie.
- Resetting the game after it's over to play again.

## Usage

To play the game, you just need to run the Python script. The game will open in a new window. 

The player (X) starts the game. Click on any of the empty cells to make your move. The AI (O) will automatically make its move after you.

The game ends when one player has three of their symbols in a row (vertically, horizontally, or diagonally), or when all cells are filled and no player has won (a tie). A message will be displayed indicating the game result. After closing this message, the game board will be reset and you can play again.

## Dependencies

This game is implemented in Python and uses the following Python libraries:

- Tkinter: For the graphical user interface.
- messagebox (from tkinter): For displaying alert messages.
- random: For making random AI moves.

These libraries are included in the standard Python distribution, so you don't need to install anything extra.

## Future improvements

The AI opponent currently makes its moves randomly. In future, it could be improved to use a smarter strategy.
