import pulp

# Parameters
M = 6  # Number of months
N = 4  # Number of investment options

# Payments required at the end of each month
payments = [0, 250000, 0, 250000, 0, 300000]

# Availability of investments (1 = available, 0 = not available)
available = [
    [1, 1, 1, 1, 1, 1],  # Investment A
    [1, 0, 1, 0, 1, 0],  # Investment B
    [1, 0, 0, 0, 1, 0],  # Investment C
    [1, 0, 0, 0, 0, 0],  # Investment D
]

# Maturity and yields for investments
maturity = [1, 2, 3, 6]  # Months to maturity
yield_rates = [0.018, 0.035, 0.058, 0.11]  # Yield at maturity

# Risk ratings for each investment
risk_ratings = [1, 3, 8, 6]  # Risk ratings for A, B, C, D

# Create the problem
problem = pulp.LpProblem("MinimizeInvestment", pulp.LpMinimize)

# Decision variables: how much to invest in each option per month
invest = pulp.LpVariable.dicts("Invest", (range(N), range(M)), lowBound=0, upBound=1000000, cat='Continuous')

# Objective: minimize total investment
total_investment = pulp.lpSum(invest[i][t] for i in range(N) for t in range(M))
problem += total_investment, "TotalInvestment"

# Constraint: ensure the investment covers the required payments at the right time
for t in range(M):
    problem += payments[t] <= pulp.lpSum(
        (invest[i][t - maturity[i]] * (1 + yield_rates[i]) if t - maturity[i] >= 0 and available[i][t - maturity[i]] else 0)
        for i in range(N)
    ), f"PaymentConstraint_{t}"

# Calculate total risk contribution
total_risk_contribution = pulp.lpSum(invest[i][t] * risk_ratings[i] for i in range(N) for t in range(M))

# Calculate total investment
total_scaled_investment = pulp.lpSum(invest[i][t] for i in range(N) for t in range(M))

# Constraint: the weighted average risk must not exceed 5
problem += total_risk_contribution <= 5 * total_scaled_investment, "RiskConstraint"

# Solve the problem
problem.solve()

# Output results
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Total Investment: {pulp.value(total_investment)}")
print("Investments per option per month:")
for i in range(N):
    for t in range(M):
        print(f"Investment {chr(65 + i)} Month {t + 1}: {invest[i][t].varValue}")

# Calculate and print weighted risk
scaled_total_investment_value = pulp.value(total_scaled_investment)
if scaled_total_investment_value > 0:
    weighted_risk = pulp.value(total_risk_contribution) / scaled_total_investment_value
else:
    weighted_risk = 0
print(f"Weighted Risk: {weighted_risk}")