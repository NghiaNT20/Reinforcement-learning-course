# Tic Tac Toe - Pygame Implementation

## 📌 Introduction
This is a simple **Tic Tac Toe** game built using Python and the `pygame` library. The game allows two players to take turns playing **X** and **O** on a **3x3 grid**, following the standard Tic Tac Toe rules.

## 🚀 Features
- **Two-player mode**: Players take turns placing `X` and `O`.
- **Automatic win detection**: The game automatically detects the winner.
- **Draw detection**: If all cells are filled without a winner, the game declares a draw.
- **Restart after game over**: The game restarts automatically after 3 seconds.
- **Graphical UI**: Uses `pygame` for drawing the grid and displaying `X` and `O` images.

## 🛠️ Installation
1. Ensure you have **Python 3** installed.
2. Install `pygame` using pip:
   ```sh
   pip install pygame
   ```
3. Download or clone this repository.
4. Place the required image assets (`modified_cover.png`, `X_modified.png`, `o_modified.png`) in the same directory as the script.

## 🎮 How to Play
1. **Run the game** by executing:
   ```sh
   python tic_tac_toe.py
   ```
2. The game starts with **X**'s turn.
3. **Click on a cell** to place `X` or `O`.
4. The game checks for a winner or draw after each move.
5. If there is a winner or a draw, the game **automatically resets** after 3 seconds.

## 🖥️ Code Overview
### **Main Components**
- `game_initiating_window()`: Displays the start screen and draws the Tic Tac Toe grid.
- `draw_status()`: Updates the message at the bottom showing whose turn it is or who won.
- `check_win()`: Checks if any player has won the game.
- `drawXO(row, col)`: Places `X` or `O` at the selected position.
- `user_click()`: Handles mouse clicks to determine where the player wants to place their mark.
- `reset_game()`: Resets the board when the game is over.

### **Game Loop**
The game runs in a loop, listening for events:
```python
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
```

## 📷 Screenshots
(Include screenshots of the game in action if possible)

## 📌 Possible Improvements
- Add an **AI opponent** using the Minimax algorithm.
- Improve UI design and animations.
- Add sound effects and background music.

## 📝 License
This project is open-source and free to use.

---
Enjoy the game! 🎮