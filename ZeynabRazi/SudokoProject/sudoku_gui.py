import tkinter as tk
import tkinter.messagebox as messagebox

class SudokuGridGUI:
    def __init__(self, root, sudoku_grid):
        self.root = root
        self.root.title("Sudoku Grid")
        self.sudoku_grid = sudoku_grid

        vcmd = (self.root.register(self.validate_input), '%P')

        self.cells = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                frame = tk.Frame(
                    root,
                    highlightbackground="black",
                    highlightthickness=1 if (i % 3 == 2 and i != 8) or (j % 3 == 2 and j != 8) else 0
                )
                frame.grid(row=i, column=j)

                entry = tk.Entry(frame, width=2, font=("Arial", 24), justify="center",
                                 validate="key", validatecommand=vcmd)

                entry.bind("<FocusOut>", lambda e, row=i, col=j: self.handle_cell_change(row, col))

                entry.grid(row=0, column=0)
                self.cells[i][j] = entry

        btn_new = tk.Button(root, text="New Puzzle", command=self.new_puzzle)
        btn_new.grid(row=9, column=0, columnspan=9)

        btn_print = tk.Button(root, text="Print Grid", command=self.print_grid)
        btn_print.grid(row=10, column=0, columnspan=9)

        btn_check = tk.Button(root, text="Check Solution", command=self.check_solution)
        btn_check.grid(row=11, column=0, columnspan=9)

    def validate_input(self, P):
        if P == "":
            return True
        if len(P) > 1:
            return False
        if P.isdigit() and 1 <= int(P) <= 9:
            return True
        return False

    def handle_cell_change(self, row, col):
        val = self.cells[row][col].get()
        if val == "":
            self.sudoku_grid.grid[row][col] = 0
            self.cells[row][col].config(bg="white")
            return

        if val.isdigit():
            num = int(val)
            if 1 <= num <= 9:
                prev = self.sudoku_grid.grid[row][col]
                self.sudoku_grid.grid[row][col] = 0
                if self.sudoku_grid.is_valid(row, col, num):
                    self.sudoku_grid.grid[row][col] = num
                    self.cells[row][col].config(bg="white")
                else:
                    self.sudoku_grid.grid[row][col] = prev
                    self.cells[row][col].config(bg="red")
                    print(f"عدد {num} در خانه ({row+1}, {col+1}) معتبر نیست.")
            else:
                self.cells[row][col].config(bg="red")
                print("لطفا عددی بین 1 تا 9 وارد کنید.")
        else:
            self.cells[row][col].config(bg="red")
            print("ورودی نامعتبر است، فقط اعداد 1 تا 9 مجاز هستند.")

    def update_grid(self):
        for i in range(9):
            for j in range(9):
                val = self.sudoku_grid.grid[i][j]
                self.cells[i][j].delete(0, tk.END)
                if val != 0:
                    self.cells[i][j].insert(0, str(val))
                self.cells[i][j].config(bg="white")

    def new_puzzle(self):
        self.sudoku_grid.fill_random_initial()
        self.update_grid()

    def print_grid(self):
        for i in range(9):
            row_values = []
            for j in range(9):
                val = self.cells[i][j].get()
                row_values.append(val if val else ".")
            print(" ".join(row_values))

    def check_solution(self):
        if self.sudoku_grid.is_complete_and_valid():
            answer = messagebox.askyesno("تبریک!", "تبریک! سودوکوت کامل و صحیحه.\nمی‌خوای دوباره بازی کنی؟")
            if answer:
                self.new_puzzle()
            else:
                self.root.destroy()
        else:
            messagebox.showinfo("ادامه بده", "سودوکوت هنوز کامل یا صحیح نیست.")
