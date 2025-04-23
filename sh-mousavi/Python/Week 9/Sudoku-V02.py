import numpy as np
import random
import turtle
from typing import List, Tuple, Optional
from numpy.typing import NDArray

# Constants
GRID_SIZE = 9
SUBGRID_SIZE = 3
EMPTY_CELL = 0

def is_valid(grid: NDArray, row: int, col: int, num: int) -> bool:
    """
    Check if placing a number in the specified position is valid.
    
    Args:
        grid: The Sudoku grid
        row: Row index
        col: Column index
        num: Number to check
        
    Returns:
        bool: True if the number can be placed, False otherwise
    """
    # Check row and column in a more concise way
    if num in grid[row, :] or num in grid[:, col]:
        return False

    # Check 3x3 sub-grid
    start_row, start_col = (row // SUBGRID_SIZE) * SUBGRID_SIZE, (col // SUBGRID_SIZE) * SUBGRID_SIZE
    return not num in grid[start_row:start_row + SUBGRID_SIZE, start_col:start_col + SUBGRID_SIZE]

def solve_grid(grid: NDArray, generate: bool = False) -> bool:
    """
    Solve or generate a Sudoku grid using backtracking.
    
    Args:
        grid: The Sudoku grid to solve/generate
        generate: If True, use random number ordering for generation
        
    Returns:
        bool: True if solution found, False otherwise
    """
    try:
        # Find first empty cell using numpy's advanced indexing
        empty_pos = np.where(grid == EMPTY_CELL)
        
        # If no empty cells found, puzzle is solved
        if not empty_pos[0].size:
            return True
            
        # Get coordinates of first empty cell
        row, col = empty_pos[0][0], empty_pos[1][0]
        
        # Create candidate numbers (random if generating, sequential if solving)
        candidates = (random.sample(range(1, GRID_SIZE + 1), GRID_SIZE) if generate 
                     else range(1, GRID_SIZE + 1))
        
        # Try each candidate number
        for num in candidates:
            # Check if number is valid in current position
            if is_valid(grid, row, col, num):
                # Place the number
                grid[row, col] = num
                
                # Recursively try to solve the rest
                if solve_grid(grid, generate):
                    return True
                    
                # If no solution found, backtrack
                grid[row, col] = EMPTY_CELL
        
        # No valid number found
        return False
        
    except Exception as e:
        print(f"An error occurred while solving: {e}")
        return False

def remove_numbers(grid: NDArray, difficulty: int = 40) -> NDArray:
    """
    Remove numbers from the grid to create a puzzle.
    
    Args:
        grid: Complete Sudoku grid
        difficulty: Number of cells to remove (higher = more difficult)
        
    Returns:
        NDArray: Grid with removed numbers
    """
    if not 0 <= difficulty <= GRID_SIZE * GRID_SIZE:
        raise ValueError(f"Difficulty must be between 0 and {GRID_SIZE * GRID_SIZE}")
        
    positions = list(np.ndindex(GRID_SIZE, GRID_SIZE))
    for pos in random.sample(positions, difficulty):
        grid[pos] = EMPTY_CELL
    return grid

def draw_sudoku_grid() -> None:
    """Draw the Sudoku grid using turtle graphics."""
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.tracer(0, 0)
    turtle.clear()
    
    # Starting position
    turtle.teleport(-180, 180)
    
    # Draw outer border
    turtle.pensize(5)
    for _ in range(4):
        turtle.forward(360)
        turtle.right(90)

    # Define grid lines with their properties (thickness, spacing)
    grid_lines = [(3, 120), (1, 40), (1, 80), (1, 160)]

    for thickness, spacing in grid_lines:
        turtle.pensize(thickness)
        for _ in range(4):
            turtle.penup()
            turtle.forward(spacing)
            turtle.right(90)
            turtle.pendown()
            turtle.forward(360)
            turtle.right(90)
            turtle.penup()
            turtle.forward(spacing)
            turtle.right(90)

    turtle.update()

def fill_sudoku_grid(sudoku: NDArray) -> None:
    """
    Fill the Sudoku grid with numbers.
    
    Args:
        sudoku: The Sudoku grid to display
    """
    turtle.hideturtle()
    cell_size = 40
    start_x, start_y = -180, 140
    
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = start_x + (col * cell_size) + 20
            y = start_y - (row * cell_size) + 6
            turtle.teleport(x, y)
            if sudoku[row, col]:
                turtle.write(sudoku[row, col], align="center", font=("Arial", 16, "normal"))
    turtle.done()

def generate_sudoku(difficulty: int = 40) -> None:
    """
    Generate and display a Sudoku puzzle.
    
    Args:
        difficulty: Number of cells to remove (higher = more difficult)
    """
    try:
        # Initialize empty grid
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        
        # Generate complete solution
        if not solve_grid(grid, generate=True):
            raise RuntimeError("Failed to generate valid Sudoku grid")
            
        # Create puzzle by removing numbers
        puzzle = remove_numbers(grid.copy(), difficulty)
        
        # Display the puzzle
        draw_sudoku_grid()
        fill_sudoku_grid(puzzle)
        
        # # Handle solution
        # if input('Do you want to solve the puzzle (y/n)? ').lower() == 'y':
        #     solution = puzzle.copy()
        #     if solve_grid(solution):
        #         print("\nSolution:")
        #         print(solution)
        #     else:
        #         print("No solution exists!")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    generate_sudoku()




