# ============================================
# Taco-Viva Construction Fund Optimization
# Linear Programming Model using PuLP
# Objective: Minimize initial investment capital
# ============================================

import pulp as pl
import pandas as pd

# Payments due at the END of each month
# Total project cost: $800,000
payments = {
    2: 250_000,  # First payment at end of month 2
    4: 250_000,  # Second payment at end of month 4
    6: 300_000  # Final payment at end of month 6
}

# Available investment instruments
# avail: months when investment can be made (at beginning of month)
# m: time to maturity (in months)
# y: yield (return rate)
# risk: risk score (1=lowest risk, 10=highest risk)
inst = {
    "A": {"avail": [1, 2, 3, 4, 5, 6], "m": 1, "y": 0.018, "risk": 1},
    "B": {"avail": [1, 3, 5], "m": 2, "y": 0.035, "risk": 3},
    "C": {"avail": [1, 4], "m": 3, "y": 0.058, "risk": 8},
    "D": {"avail": [1], "m": 6, "y": 0.11, "risk": 6},
}

# Planning horizon (6 months)
T = 6


def solve_taco_viva(max_risk_allowed=5, verbose=False):
    """
    Solve the optimization problem to find minimum initial investment

    Parameters:
        max_risk_allowed: Maximum allowed weighted-average risk
        verbose: Whether to display solver details

    Returns:
        I0_val: Minimum required initial capital
        df_inv: Optimal investment schedule DataFrame
        df_paths: Payment allocation paths DataFrame
        risk_avg: Weighted average risk of investments
    """

    # ============================================
    # Decision Variables
    # ============================================

    # Variable x[i,t]: Amount invested in instrument i at month t
    x = {}
    for i, data in inst.items():
        for t in data["avail"]:
            x[(i, t)] = pl.LpVariable(f"x_{i}_{t}", lowBound=0, cat='Continuous')

    # Variable I0: Initial capital (objective to minimize)
    I0 = pl.LpVariable("I0", lowBound=0, cat='Continuous')

    # Variable b[t]: Cash balance at beginning of month t
    b = {t: pl.LpVariable(f"b_{t}", lowBound=0, cat='Continuous')
         for t in range(1, T + 2)}

    # ============================================
    # Linear Programming Model
    # ============================================
    model = pl.LpProblem("TacoViva_MinInitial", pl.LpMinimize)

    # Objective function: Minimize initial capital
    model += I0

    # Constraint 1: Initial balance equals initial capital
    model += b[1] == I0

    # ============================================
    # Monthly Cash Flow Constraints
    # ============================================
    for t in range(1, T + 1):
        # Funds maturing this month (from previous investments)
        maturities = []
        for i, data in inst.items():
            m = data["m"]  # Time to maturity
            y = 1 + data["y"]  # Gross return multiplier
            s = t - m  # Investment month
            if s in data["avail"]:  # If investment was allowed in month s
                maturities.append(x[(i, s)] * y)

        # New investments made this month
        purchases = []
        for i, data in inst.items():
            if t in data["avail"]:
                purchases.append(x[(i, t)])

        # Payment due this month (if any)
        payment_t = payments.get(t, 0)

        # Cash flow balance equation:
        # Beginning balance + maturing funds - new investments - payment = Ending balance
        model += (b[t] + pl.lpSum(maturities) -
                  pl.lpSum(purchases) - payment_t == b[t + 1])

    # ============================================
    # Risk Constraint
    # ============================================

    # Total investment amount
    sum_x = pl.lpSum(x.values())

    # Weighted risk sum (risk of each investment multiplied by its amount)
    sum_riskx = pl.lpSum(inst[i]["risk"] * x[(i, t)] for (i, t) in x)

    # Constraint: Weighted average risk must be <= maximum allowed risk
    # Equivalent to: sum_riskx <= max_risk_allowed * sum_x
    model += sum_riskx <= max_risk_allowed * sum_x, "Risk_Constraint"

    # ============================================
    # Solve the Model
    # ============================================
    status = model.solve(pl.PULP_CBC_CMD(msg=False))

    if verbose:
        print("Solver status:", pl.LpStatus[model.status])

    # Check for optimal solution
    if pl.LpStatus[model.status] != "Optimal":
        raise RuntimeError(f"Solver failed with status: {pl.LpStatus[model.status]}")

    # ============================================
    # Extract Results
    # ============================================

    # Optimal initial capital value
    I0_val = pl.value(I0)

    # Create list of investments made
    investments = []
    for (i, t), var in x.items():
        v = var.value()
        if v and v > 1e-6:  # Only include significant values
            investments.append({
                "Instrument": i,
                "Investment_Month": t,
                "Maturity_Month": t + inst[i]['m'],
                "Investment_Amount": v,
                "Yield_Rate": inst[i]['y'],
                "Final_Value": v * (1 + inst[i]['y']),
                "Risk": inst[i]['risk']
            })

    # Create DataFrame from investment results
    df_inv = pd.DataFrame(investments)

    # Calculate weighted average risk
    total_investment = pl.value(sum_x)
    total_risk_weighted = pl.value(sum_riskx)
    risk_avg = total_risk_weighted / total_investment if total_investment > 0 else 0

    # ============================================
    # Payment Path Analysis
    # ============================================
    payment_paths = []

    # For each payment, determine which investments funded it
    for pay_month, pay_amount in payments.items():
        remaining = pay_amount  # Remaining payment amount

        # Investments that mature in this payment month
        sources = df_inv[df_inv['Maturity_Month'] == pay_month].copy()

        # Allocate payment from maturing investments
        for idx, row in sources.iterrows():
            src_value = row['Final_Value']
            used_value = min(src_value, remaining)  # Amount used from this source

            payment_paths.append({
                "Payment_Month": pay_month,
                "Payment_Amount": pay_amount,
                "Source_Instrument": row['Instrument'],
                "Investment_Month": row['Investment_Month'],
                "Invested_Amount": row['Investment_Amount'],
                "Yield_Rate": row['Yield_Rate'],
                "Maturity_Month": row['Maturity_Month'],
                "Covered_Amount": used_value
            })

            remaining -= used_value
            if remaining <= 1e-6:  # If payment is fully covered
                break

    # Create DataFrame from payment paths
    df_paths = pd.DataFrame(payment_paths)

    return I0_val, df_inv, df_paths, risk_avg


# ============================================
# Run Different Scenarios
# ============================================

if __name__ == "__main__":
    # Different risk tolerance levels to analyze
    risk_limits = [4, 5, 6]
    results_summary = []

    print("Analysis of Different Risk Tolerance Scenarios")
    print("=" * 60)

    # Run model for each risk level
    for r in risk_limits:
        I0_val, df_inv_temp, df_paths_temp, risk_avg = solve_taco_viva(max_risk_allowed=r)
        results_summary.append({
            "Max_Risk_Allowed": r,
            "Min_Initial_Capital": I0_val,
            "Achieved_Risk_Avg": risk_avg
        })

    # Create summary results table
    summary_df = pd.DataFrame(results_summary)

    print("\nSummary of Different Scenarios:")
    print("=" * 60)
    print(summary_df.to_string(index=False))

    # Display detailed results for main scenario (Risk = 5)
    print("\n" + "=" * 60)
    print("Detailed Results for Risk Tolerance = 5")
    print("=" * 60)

    I0_val, df_inv, df_paths, risk_avg = solve_taco_viva(max_risk_allowed=5)

    print(f"\nMinimum Initial Investment Required: ${I0_val:,.2f}")
    print(f"Weighted Average Risk: {risk_avg:.3f}")

    print("\nOptimal Investment Schedule:")
    print("-" * 60)
    if not df_inv.empty:
        # Format numbers for better display
        df_display = df_inv.copy()
        df_display['Investment_Amount'] = df_display['Investment_Amount'].apply(lambda x: f"${x:,.2f}")
        df_display['Final_Value'] = df_display['Final_Value'].apply(lambda x: f"${x:,.2f}")
        df_display['Yield_Rate'] = df_display['Yield_Rate'].apply(lambda x: f"{x:.1%}")
        print(df_display.to_string(index=False))
    else:
        print("No investments made.")

    print("\nPayment Funding Paths:")
    print("-" * 60)
    if not df_paths.empty:
        df_paths_display = df_paths.copy()
        df_paths_display['Payment_Amount'] = df_paths_display['Payment_Amount'].apply(lambda x: f"${x:,.2f}")
        df_paths_display['Invested_Amount'] = df_paths_display['Invested_Amount'].apply(lambda x: f"${x:,.2f}")
        df_paths_display['Covered_Amount'] = df_paths_display['Covered_Amount'].apply(lambda x: f"${x:,.2f}")
        df_paths_display['Yield_Rate'] = df_paths_display['Yield_Rate'].apply(lambda x: f"{x:.1%}")
        print(df_paths_display.to_string(index=False))
    else:
        print("No payment paths found.")














