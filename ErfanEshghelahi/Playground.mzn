% Number of months and investments
int: M = 6;  % Number of months
int: N = 4;  % Number of investment options

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

% Decision variables: how much to invest in each option per month
array[1..N, 1..M] of var 0.0..1000000.0: invest;

% Objective: minimize total investment
var float: total_investment = sum(i in 1..N, t in 1..M) (invest[i, t]);

% Constraint: ensure the investment covers the required payments at the right time
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