int: M = 6;  % Number of months
int: N = 4;  % Number of investment options
% Enable quadratic constraints (if your solver supports it)
constraint QuadrFloat = true;
% Payments required at the end of each month
array[1..M] of float: payments = [0, 250000, 0, 250000, 0, 300000];

% Availability of investments (boolean array)
array[1..N, 1..M] of bool: available = 
   [| true, true, true, true, true, true |   % Investment A
    true, false, true, false, true, false | % Investment B
    true, false, false, false, true, false | % Investment C
    true, false, false, false, false, false |]; % Investment D

% Maturity and yields for investments
array[1..N] of int: maturity = [1, 2, 3, 6]; % Months to maturity
array[1..N] of float: yield = [0.018, 0.035, 0.058, 0.11]; % Yield at maturity

% Risk ratings for each investment
array[1..N] of int: risk_ratings = [1, 3, 8, 6]; % Risk ratings for A, B, C, D

% Decision variables: how much to invest in each option per month
array[1..N, 1..M] of var 0.0..1000000.0: invest;

% Objective: minimize total investment
var float: total_investment = sum(i in 1..N, t in 1..M) (invest[i, t]);

% Declare the scaled decision variables
array[1..N, 1..M] of var int: invest_scaled;

% Total investment for each option
array[1..N] of var float: total_investments = [sum(t in 1..M) (invest[i, t]) | i in 1..N];

% Reformulate the weighted risk constraint
var int: total_risk_contribution = sum(i in 1..N)(risk_ratings[i] * round(sum(t in 1..M)(invest[i, t])));
var int: total_scaled_investment = sum(i in 1..N)(round(sum(t in 1..M)(invest[i, t])));
var float: weighted_risk = total_risk_contribution / total_scaled_investment;

% Ensure the weighted risk does not exceed 5
constraint weighted_risk <= 5;

% Ensure the investments cover the required payments at the right time
constraint
  forall(t in 1..M)(
    payments[t] <= sum(i in 1..N)
      (if (t - maturity[i] + 1 > 0) /\ available[i, t - maturity[i] + 1] 
       then invest[i, t - maturity[i] + 1] * (1 + yield[i]) 
       else 0.0 
       endif)
  );

% Solve the optimization problem to minimize total initial investment
solve minimize total_investment;

% Output the results
output [
  "Total Investment: ", show(total_investment), "\n",
  "Weighted Risk: ", show(weighted_risk), "\n",
  "Investments: \n"
] ++ 
[ if i == 1 then "Investment " ++ show(i) ++ ": " else "" endif ++ 
  show([round(invest[i, t]) | t in 1..M]) ++ "\n" | i in 1..N ];