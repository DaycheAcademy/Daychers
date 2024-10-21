import pulp as lp
import pandas as pd

# Load the CSV file into a DataFrame
distance_df = pd.read_csv('distances.csv', index_col=0)

# Define costs
direct_cost = 0.0015
hub_cost = 0.0003
amman_to_dubai_cost = 0.0022

# Client demands and prices
clients = {
    'Munich': {'demand': 5400, 'price': 30.61},
    'Hamburg': {'demand': 6300, 'price': 31.47},
    'Bologna': {'demand': 6700, 'price': 29.87},
    'Moscow': {'demand': 4100, 'price': 24.96},
    'Dubai': {'demand': 7800, 'price': 34.65},
    'Beijing': {'demand': 9600, 'price': 19.17},
    'Kyoto': {'demand': 8200, 'price': 38.88}
}

# Production facilities and hubs
facilities = ['Hannover', 'Hyderabad']
hubs = ['Amman', 'St. Petersburg']

# Decision variables: Amount of units transported from facility/hub to client
x = lp.LpVariable.dicts("x", [(f, c) for f in facilities + hubs for c in clients], lowBound=0, cat='Continuous')

# Create the problem
prob = lp.LpProblem("Floodlight_Production_Optimization", lp.LpMaximize)

# Revenue: Calculate the total revenue for each client
total_revenue = lp.lpSum([x[(f, c)] * clients[c]['price'] for f in facilities + hubs for c in clients])
print(total_revenue)
# Transportation cost: As before, minimizing the total transportation cost
total_transportation_cost = lp.lpSum([x[(f, c)] * distance_df.loc[f, c] * (direct_cost if f in facilities else hub_cost)
                                      for f in facilities for c in clients] +
                                     [x[('Amman', 'Dubai')] * distance_df.loc['Amman', 'Dubai'] * amman_to_dubai_cost] +
                                     [x[(f, c)] * distance_df.loc[f, c] * hub_cost for f in hubs for c in clients if c != 'Dubai'])

# Objective function: Maximize profit (Revenue - Transportation cost)
prob += total_revenue - total_transportation_cost

# Constraints:
# - Demand must be met at least 90% but not exceed full demand
for c in clients:
    prob += lp.lpSum([x[(f, c)] for f in facilities + hubs]) >= 0.9 * clients[c]['demand'], f"Demand_{c}_min"
    prob += lp.lpSum([x[(f, c)] for f in facilities + hubs]) <= clients[c]['demand'], f"Demand_{c}_max"

# - Hub capacity: No more than 22,000 units passing through each hub
for h in hubs:
    prob += lp.lpSum([x[(h, c)] for c in clients]) <= 22000, f"HubCapacity_{h}"

# - European and Russian import restriction to Beijing (max 5000 units)
prob += lp.lpSum([x[(f, 'Beijing')] for f in ['Hannover', 'St. Petersburg']]) <= 5000, "China_Import_Restriction"

# - No transport from Europe to Russia
prob += x[('Hannover', 'Moscow')] == 0, "No_Transport_Europe_Russia"
# Constraint: No transport from St. Petersburg to European clients
# european_clients = ['Munich', 'Hamburg', 'Bologna']
#
# for client in european_clients:
#     prob += x[('St. Petersburg', client)] == 0, f"No_Transport_StPetersburg_to_{client}"
# Solve the problem
prob.solve()

# Output the results
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the total transportation cost and profit
print("Total Transportation Cost =", lp.value(total_transportation_cost))
print("Total Profit =", lp.value(prob.objective))