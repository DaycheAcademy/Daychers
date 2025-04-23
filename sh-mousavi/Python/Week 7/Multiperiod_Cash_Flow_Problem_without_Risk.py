import numpy as np
from scipy.optimize import linprog

# Objective function coefficients (minimizing total investment)
c = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]  # Minimize (x_A1 + x_B1 + x_C1 + x_D1)

# Equality constraint coefficients (A_eq * x = b_eq)
A_eq = [
    [1.018, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],             # x_A1 * 1.018 - x_A2 = 0
    [0, 1.018, -1, 0, 0, 0, 1.035, -1, 0, 0, 0, 0],        # x_A2 * 1.018 - x_A3 + x_B1 * 1.035 - x_B3 = 250000
    [0, 0, 1.018, -1, 0, 0, 0, 0, 0, 1.058, -1, 0],        # x_A3 * 1.018 - x_A4 + x_C1 * 1.058 - x_C4 = 0
    [0, 0, 0, 1.018, -1, 0, 0, 1.035, -1, 0, 0, 0],        # x_A4 * 1.018 - x_A5 + x_B3 * 1.035 - x_B5 = 250000
    [0, 0, 0, 0, 1.018, -1, 0, 0, 0, 0, 0, 0],             # x_A5 * 1.018 - x_A6 = 0
    [0, 0, 0, 0, 0, 1.018, 0, 0, 1.035, 0, 1.058, 1.11]    # x_A6 * 1.018 + x_B5 * 1.035 + x_C4 * 1.058 + x_D1 * 1.11 = 300000
]

b_eq = [0, 250000, 0, 250000, 0, 300000]

# Bounds (ensuring investments are non-negative)
x_bounds = [(0, None)] * 12  # Bounds for all 12 variables

# Solve the LP problem
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method="highs")

# Display results
if result.success:
    print(result.x)
    print("✅ Optimal Investment Plan:")
    print(f"Investment in A: {result.x[0]:,.2f}")
    print(f"Investment in B: {result.x[6]:,.2f}")
    print(f"Investment in C: {result.x[9]:,.2f}")
    print(f"Investment in D: {result.x[11]:,.2f}")
    print(f"🔹 Total Initial Investment: {result.fun:,.2f}")
else:
    print("❌ Optimization Failed! Check the model formulation.")
