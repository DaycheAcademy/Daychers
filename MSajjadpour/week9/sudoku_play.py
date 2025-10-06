
import turtle
import random
import time
import copy

# -------------------------------
# CONFIG
# -------------------------------
N = 9              # Sudoku size
W = 40             # Cell width
ratio = W // 8     # Font ratio


# -------------------------------
# DRAW GRID
# -------------------------------
def draw_grid(pen: turtle.Turtle) -> None:
    """Draws a Sudoku grid with bold lines every 3 cells."""
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-N * W / 2, N * W / 2)  # top-left corner
    pen.pendown()

    # Outer border
    pen.pensize(5)
    for _ in range(4):
        pen.forward(N * W)
        pen.right(90)

    # Vertical + horizontal lines
    for i in range(1, N):
        # Vertical
        pen.pensize(3 if i % 3 == 0 else 1)
        pen.penup()
        pen.goto(-N * W / 2 + i * W, N * W / 2)
        pen.pendown()
        pen.goto(-N * W / 2 + i * W, -N * W / 2)

        # Horizontal
        pen.pensize(3 if i % 3 == 0 else 1)
        pen.penup()
        pen.goto(-N * W / 2, N * W / 2 - i * W)
        pen.pendown()
        pen.goto(N * W / 2, N * W / 2 - i * W)


def goto_xy(pen: turtle.Turtle, x: int, y: int):
    """Move pen to the center of cell (x,y)."""
    xpos = -N * W / 2 + (x + 0.5) * W
    ypos = N * W / 2 - (y + 0.8) * W
    pen.penup()
    pen.setposition(xpos, ypos)


def write_numbers(pen: turtle.Turtle, num: int, x: int, y: int, color: str = "black"):
    """Write a number in Sudoku grid."""
    goto_xy(pen, x, y)
    pen.color(color)
    if num != 0:
        pen.write(num, align="center", font=("Verdana", 12, "normal"))


# -------------------------------
# SUDOKU LOGIC
# -------------------------------
def valid(grid, row, col, num):
    """Check if placing num at (row,col) is valid."""
    # Row
    if num in grid[row]:
        return False
    # Col
    if num in [grid[r][col] for r in range(9)]:
        return False
    # Square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True


def solve(grid):
    """Backtracking Sudoku solver."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


def generate_full_grid():
    """Generate a full valid Sudoku grid."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve(grid)  # fill with valid solution
    return grid


def make_puzzle(grid, attempts=40):
    """Remove numbers from grid to create puzzle."""
    puzzle = copy.deepcopy(grid)
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while puzzle[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        puzzle[row][col] = 0
        attempts -= 1
    return puzzle


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    turtle.tracer(0)

    # Draw the Sudoku grid
    grid_pen = turtle.Turtle()
    draw_grid(grid_pen)

    # Generate full grid
    full_grid = generate_full_grid()

    # Make puzzle
    puzzle = make_puzzle(full_grid, attempts=40)

    # Write puzzle on board
    num_pen = turtle.Turtle()
    num_pen.hideturtle()
    for r in range(9):
        for c in range(9):
            write_numbers(num_pen, puzzle[r][c], c, r, "black")

    turtle.update()
    time.sleep(3)

    # Solve puzzle and show in green
    solved = copy.deepcopy(puzzle)
    solve(solved)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                write_numbers(num_pen, solved[r][c], c, r, "green")

    turtle.update()
    turtle.done()
