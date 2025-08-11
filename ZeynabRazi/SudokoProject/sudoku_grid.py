import random

class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid(self, row, col, num):
        # چک ردیف
        if num in self.grid[row]:
            return False
        
        # چک ستون
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        
        # چک مربع 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        
        return True
    
    def fill_random_initial(self, count=25):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
        attempts = 0
        filled = 0
        while filled < count and attempts < count * 10:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            if self.grid[row][col] == 0 and self.is_valid(row, col, num):
                self.grid[row][col] = num
                filled += 1
            attempts += 1
    
    def is_complete_and_valid(self):
        for i in range(9):
            for j in range(9):
                num = self.grid[i][j]
                if num == 0:
                    return False
                self.grid[i][j] = 0
                if not self.is_valid(i, j, num):
                    self.grid[i][j] = num
                    return False
                self.grid[i][j] = num
        return True
