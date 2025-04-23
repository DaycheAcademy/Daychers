import numpy as np
import random
import turtle

def is_valid(grid, row, col, num):
    """Checks if placing 'num' in grid[row][col] is valid."""
    # Check row and column
    if num in grid[row, :] or num in grid[:, col]:
        return False

    # Check 3x3 sub-grid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    if num in grid[start_row:start_row + 3, start_col:start_col + 3]:
        return False

    return True


def solve(grid):
    """Recursive function to fill the Sudoku board using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:  # Find an empty cell
                for num in random.sample(range(1, 10), 9):  # Try numbers randomly
                    if is_valid(grid, row, col, num):
                        grid[row, col] = num
                        if solve(grid):  # Recursively solve the rest
                            return True
                        grid[row, col] = 0  # Backtrack if no solution
                return False  # No valid number found, trigger backtracking
    return True  # Solution found


def draw_sudoku_grid():
    """Draw a Sudoku grid."""
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.tracer(0, 0)  # Disable real-time drawing
    turtle.clear()

    turtle.teleport(-180, 180)

    turtle.pensize(5)
    for _ in range(4):
        turtle.forward(360)
        turtle.right(90)

    grid_lines = [(3, 120), (1, 40), (1, 80), (1, 160)]

    for item in grid_lines:
        turtle.pensize(item[0])
        for _ in range(4):
            turtle.penup()
            turtle.forward(item[1])
            turtle.right(90)
            turtle.pendown()
            turtle.forward(360)
            turtle.right(90)
            turtle.penup()
            turtle.forward(item[1])
            turtle.right(90)

    turtle.update()  # Display final result


def fill_sudoku_grid(sudoku):
    """Fill the Sudoku table with numbers."""
    turtle.hideturtle()

    x, y = -180, 140

    for row in range(9):
        for col in range(9):
            turtle.teleport(x + 20, y + 6)
            if sudoku[row, col]:
                turtle.write(sudoku[row, col], align="center", font=("Arial", 16, "normal"))
            x += 40
        x = -180
        y -= 40
    turtle.done()

def generate_sudoku():
    """Generates a complete valid Sudoku board."""
    grid = np.zeros((9, 9), dtype=int)
    solve(grid)  # Fill the board using backtracking
    print("Generated Sudoku Board:")
    print(grid)

    # Draw Sudoku Table
    draw_sudoku_grid()

    # Fill the Sudoku Table
    fill_sudoku_grid(grid)


if __name__ == '__main__':

    generate_sudoku()




