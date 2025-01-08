import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x400")
        self.master.configure(bg='lightblue')

        self.current_player = 'X'  # Human player
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(master, text=' ', font=('Arial', 60), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c), bg='yellow', fg='black')
                button.grid(row=row, column=col, sticky="nsew")  # Fill the entire grid cell
                self.buttons[row][col] = button

        # Make rows and columns expand to fill the window
        for i in range(3):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def player_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X', fg='blue')
            if self.check_winner() == 'X':
                messagebox.showinfo("Game Over", "Congratulations! You won!")
                self.reset_game()
                return
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            self.ai_move()
            if self.check_winner() == 'O':
                messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
                self.reset_game()

    def ai_move(self):
        best_score = -float('inf')
        best_move = (-1, -1)
        
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'  # AI's move
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = ' '  # Undo move
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        row, col = best_move
        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O', fg='red')
        if self.check_winner() == 'O':
            messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
            self.reset_game()
        elif self.is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner() == 'O':
            return 1  # AI wins
        elif self.check_winner() == 'X':
            return -1  # Human wins
        elif self.is_full():
            return 0  # Draw

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None  # No winner yet

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')
                
def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()