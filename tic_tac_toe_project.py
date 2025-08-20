import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self.current = "X"
        self.moves = 0
        self.board = [""] * 9
        self.buttons = []

        # UI: title, grid, status, controls
        title = tk.Label(root, text="Tic Tac Toe", font=("Segoe UI", 18, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=(8, 4))

        self.status = tk.Label(root, text="Player X turn", font=("Segoe UI", 12))
        self.status.grid(row=1, column=0, columnspan=3, pady=(0, 6))

        for i in range(9):
            btn = tk.Button(
                root, text="", width=6, height=3,
                font=("Segoe UI", 20, "bold"),
                command=lambda i=i: self.play(i)
            )
            r, c = divmod(i, 3)
            btn.grid(row=r + 2, column=c, padx=3, pady=3)
            self.buttons.append(btn)

        ctrl = tk.Frame(root)
        ctrl.grid(row=5, column=0, columnspan=3, pady=(6, 10))
        tk.Button(ctrl, text="Reset", width=10, command=self.reset).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="Quit", width=10, command=root.destroy).pack(side=tk.LEFT, padx=5)

        self.x_score = 0
        self.o_score = 0
        self.score_lbl = tk.Label(root, text=self._score_text(), font=("Segoe UI", 11))
        self.score_lbl.grid(row=6, column=0, columnspan=3, pady=(0, 8))

    def _score_text(self):
        return f"Score  X: {self.x_score}   O: {self.o_score}"

    def play(self, i):
        if self.board[i] != "":
            return
        self.board[i] = self.current
        self.buttons[i]["text"] = self.current
        self.buttons[i]["state"] = "disabled"
        self.moves += 1

        winner = self.check_winner()
        if winner:
            self.end_game(f"Player {winner} wins!")
            if winner == "X":
                self.x_score += 1
            else:
                self.o_score += 1
            self.score_lbl.config(text=self._score_text())
            return

        if self.moves == 9:
            self.end_game("It's a draw!")
            return

        self.current = "O" if self.current == "X" else "X"
        self.status.config(text=f"Player {self.current} turn")

    def check_winner(self):
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                # highlight winning line
                for idx in (a, b, c):
                    self.buttons[idx].config(bg="#d1ffd1")
                return self.board[a]
        return None

    def end_game(self, msg):
        self.status.config(text=msg)
        for btn in self.buttons:
            btn["state"] = "disabled"
        # Show a non-blocking info; comment out if you prefer no popup
        messagebox.showinfo("Game Over", msg)

    def reset(self):
        self.current = "X"
        self.moves = 0
        self.board = [""] * 9
        self.status.config(text="Player X turn")
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
