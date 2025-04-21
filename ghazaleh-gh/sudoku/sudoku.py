import turtle
from random import choice, sample
from copy import deepcopy
from time import sleep


class sudoku:
    def __init__(self, size_of_table: int =750, box: int =3, grid: int =9 ):
        self.sizeOfTable = size_of_table
        self.box = box
        self.grid = grid
        self.draw = turtle.Turtle()
        # self.write_numbers = turtle.Turtle()
        # self.write_answers = turtle.Turtle()
        self.write = turtle.Turtle()
        self.numbers = set(range(1, 10))
        self.mat = [[0 for _ in range(9)] for _ in range(9)]
        self.start = (self.draw.pos()[0] - self.sizeOfTable / 2, self.draw.pos()[1] + self.sizeOfTable / 2)

    def generate(self):
        self.initial()
        # create the table for sudoku
        self.draw.begin_fill()
        self.draw_table()
        self.draw_lines(3, 'horizontal', True)
        self.draw_lines(3, 'vertical', True)
        self.draw_lines(1, 'horizontal')
        self.draw_lines(1, 'vertical')
        self.draw.end_fill()

        # create the full matrix of a sudoku and then remove some cells
        self.generate_sudoku()
        self.clear_squares()
        self.fill_grid(mode='create')

        # activating the animation of turtle with delay
        turtle.tracer(1, 100)

        # after 3Sec of waiting the matrix of sudoku will be solves and the answer will be written in the table
        sleep(3)
        cells_to_fill = self.solve()
        self.fill_grid('solve', cells_to_fill)

        turtle.done()

    def initial(self):
        turtle.title('Sudoku Game')
        turtle.Screen().bgcolor('#f2ffff')
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.draw.hideturtle()
        # self.write_answers.hideturtle()
        # self.write_numbers.hideturtle()
        self.write.hideturtle()

    def draw_table(self):
        self.draw.color('#457b9d')  # color of the lines of table
        self.draw.fillcolor('#d9feff')  # color to fill the table
        self.draw.teleport(self.start[0], self.start[1])
        for _ in range(4) :
            self.draw.width(5)
            self.draw.forward(self.sizeOfTable)
            self.draw.right(90)

    def draw_lines(self, width, direction, box_line=False):
        self.draw.setheading(0)
        self.draw.width(width)
        if box_line:
            sizeOfSquare = self.sizeOfTable / self.box
        else:
            sizeOfSquare = self.sizeOfTable / self.grid

        if 'h' in direction.lower():
            self.draw.teleport(self.start[0], self.start[1] - sizeOfSquare)
            while self.draw.pos()[1] >= -(self.sizeOfTable - self.start[1]) :
                self.draw.forward(self.sizeOfTable)
                self.draw.teleport(x=self.start[0], y=self.draw.pos()[1] - sizeOfSquare)
        elif 'v' in direction.lower():
            self.draw.teleport(self.start[0] + sizeOfSquare, self.start[1])
            self.draw.right(90)
            while self.draw.pos()[0] <= self.sizeOfTable - abs(self.start[0]) :
                self.draw.forward(self.sizeOfTable)
                self.draw.teleport(x=self.draw.pos()[0] + sizeOfSquare, y=self.start[1])

    def check_row(self, row: int, col: int) -> bool:
        value = self.mat[row][col]

        if self.mat[row].count(value) > 1:
            # print("check_row: false", end=" | ")
            return False

        return True

    def check_col(self, row: int, col: int) -> bool:
        value = self.mat[row][col]
        column = [self.mat[i][col] for i in range(9)]

        if column.count(value) > 1:
            # print("check_col: false", end=" | ")
            return False
        return True

    def check_box(self, row, col):
        box_row = (row // 3) * 3  # Starting row of the 3x3 box
        box_col = (col // 3) * 3  # Starting column of the 3x3 box
        value = self.mat[row][col]
        box = [self.mat[box_row + r][box_col + c] for r in range(3) for c in range(3)]  # Extract the 3x3 box as a list

        count = box.count(value)
        if count > 1:
            # print("check_box: false", end=" | ")
            return False  # If the count is greater than 1, the value is duplicated
        return True

    def backtrack(self, row, col):
        if col == 0:
            row -= 1
            col = 8
            # print(f"cell[{row}][{col}]is reseting!", end=" | ")

        else:
            col -= 1
            # print(f"cell[{row}][{col}]is reseting!", end=" | ")

        self.mat[row][col] = 0
        # return row, col

    def generate_sudoku(self):
        prev_answers = {i: set() for i in range(81)}
        cell_index = 0
        while cell_index < 81:

            row = cell_index // 9
            col = cell_index % 9

            if self.mat[row][col] == 0:
                avail_nums = self.numbers - prev_answers[cell_index]
                # print("avail_nums : ", avail_nums)

                if not bool(avail_nums):
                    # print("backtracking...", end=" | ")
                    prev_answers[cell_index] = set()
                    # row, col = self.backtrack(row, col, 'create')
                    # cell_index = row * 9 + col
                    self.backtrack(row, col)
                    cell_index -= 1
                    continue

                self.mat[row][col] = choice(list(avail_nums))
                prev_answers[cell_index].add(self.mat[row][col])

                # print(f"[{row}][{col}]->{self.mat[row][col]}", end=" | ")

                if not (self.check_row(row, col) and self.check_col(row, col) and self.check_box(row, col)):
                        self.mat[row][col] = 0
                        # print("choosing another value...", end=" | ")
                else:
                    cell_index += 1

        # print()
        # print("----FINAL GENERATED MATRIX (self.mat)----")
        # for h in self.mat:
        #     print(h)

    def clear_squares(self):

        all_positions = [(x, y) for x in range(9) for y in range(9)]

        selected_positions = sample(all_positions, 40)

        row_x, col_y = zip(*selected_positions)

        # print("coordinates to be removed:", end=" ")
        # for X, Y in sorted(list(zip(row_x, col_y))) :
        #     print(f"x:{X},y:{Y}", end=" | ")
        # print()

        for x, y in zip(row_x, col_y) :
            self.mat[x][y] = 0


        # print("\n")
        # print("----FINAL GENERATED SUDOKU (self.mat)----")
        # for i in self.mat :
        #     print(i)

    def find_previous_empty_cell(self, i, empty_cells_index):

        while i-1 not in empty_cells_index:
            i -= 1
        return i


    def solve(self):
        # prev_row_values = {i: (set(self.mat[i])) for i in range(9)}
        # print("existing  values for rows:", prev_row_values)
        # prev_col_values = {i: (set(self.mat[j][i] for j in range(9))) for i in range(9)}
        # print("existing values for cols:", prev_col_values)

        empty_cells_index = [i * 9 + j for i, x in enumerate(self.mat) for j, y in enumerate(x) if not y]

        prev_answers = {i: set() for i in range(81)}
        cell_index = 0

        while cell_index < 81:
            row = cell_index // 9
            col = cell_index % 9

            if self.mat[row][col] == 0:
                avail_nums = self.numbers - prev_answers[cell_index]
                # print(f"avail_nums  for {cell_index}: {avail_nums}")

                if not bool(avail_nums):
                    # print("backtracking...", end=" | ")
                    prev_answers[cell_index] = set()
                    cell_index = self.find_previous_empty_cell(cell_index, empty_cells_index)
                    self.backtrack(cell_index // 9, cell_index % 9)
                    cell_index -= 1

                    continue

                self.mat[row][col] = choice(list(avail_nums))
                prev_answers[cell_index].add(self.mat[row][col])

                # print(f"[{row}][{col}]->{self.mat[row][col]}", end=" | ")

                if not (self.check_row(row, col) and self.check_col(row, col) and self.check_box(row, col)):

                    self.mat[row][col] = 0
                    # print("choosing another value...", end=" | ")
                else:
                    cell_index += 1
            else:
                cell_index += 1

        # print("\n")
        # print("----FINAL SOLVED MATRIX----")
        # for h in self.mat:
        #     print(h)
        return empty_cells_index

    def fill_grid(self, mode, cells_index_to_fill=[]):
        start_x = self.start[0]
        start_y = self.start[1]
        size = self.sizeOfTable / self.grid
        self.write.setheading(0)

        if mode =='create':
            cells_index_to_fill = [i * 9 + j for i, x in enumerate(self.mat) for j, y in enumerate(x) if y]
            # print(cells_index_to_fill)
            self.write.color('#1d3557')

        elif mode == 'solve':
            # print(cells_index_to_fill)
            self.write.color('#e63946')

        for index in cells_index_to_fill:
            row = index // 9
            col = index % 9
            self.write.teleport(start_x + size * (col + 1 / 2), start_y - size * row - size / 1.5)
            self.write.write(self.mat[row][col], align='center', font=('Arial', int(size / 4.5), 'bold'))



def main():
    sudoku_instance = sudoku()
    sudoku_instance.generate()


if __name__ == '__main__':
    main()
