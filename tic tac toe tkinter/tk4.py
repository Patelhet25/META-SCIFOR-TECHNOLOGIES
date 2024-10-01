import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        # Create reset button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.pack(pady=10)

        # Create a frame for the board
        frame = tk.Frame(self.root)
        frame.pack()

        # Create buttons for the Tic Tac Toe grid
        for i in range(9):
            button = tk.Button(frame, text="", font=("Arial", 24), width=3, height=1,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_click(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)


if __name__ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()