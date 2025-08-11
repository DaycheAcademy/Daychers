import tkinter as tk
from sudoku_grid import SudokuGrid
from sudoku_gui import SudokuGridGUI

def main():
    sudoku = SudokuGrid()
    sudoku.fill_random_initial()

    root = tk.Tk()
    gui = SudokuGridGUI(root, sudoku)
    gui.update_grid()

    root.mainloop()

if __name__ == "__main__":
    main()
