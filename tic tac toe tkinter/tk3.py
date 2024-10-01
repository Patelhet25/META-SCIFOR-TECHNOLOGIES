import tkinter as tk
from tkinter import messagebox

class tic_tac_toe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tictactoe")
        self.current_player = "X"


        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window,text=" ",font=("Arial", 20),
                width=10,height=5,command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                self.reset_game()
            elif self.check_draw():
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] != " "
            or self.board[0][2] == self.board[1][1] == self.board[2][0] != " "
        ):
            return True
        return False
    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "


if __name__ == "__main__":
    game = tic_tac_toe()
    game.window.mainloop()