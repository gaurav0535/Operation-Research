"""
Name    Cost
Chicken .013
Beef    .008
Mutton  .010
Rice    .002
Wheat   .005
Gel     .001
All the costs are per gram

Stuff       Protein     Fat         Fibre          Salt
Chicken     .1          .080        .001            .002
Beef        .2          .10         .005            .005
Rice        .000        .010        .100            .002
Wheat bran  .040        .010        .150            .008

Assumptions :
    x1 : percentage of chicken
    x2 : percentage of beef

Objective Function :
    min 0.013x1 + 0.008x2

Constraints :

    The constraints on the variables are that they must sum to 100 and that nutritional requirements are met:

    1x1 + 1x2 = 100
    1x1 + .2x2 >= 8
    .08x1 +.1x2 >= 6
    .001x1 + .005x2 =< 2.0
    .002x1 + .005x2 =< .4
"""

from pulp import *


prob = LpProblem("The Whiskas Problem", LpMinimize)


# The 2 variables Beef and Chicken are created with a lower limit of zero
x1 = LpVariable("ChickenPercent", 0, None, LpInteger)
x2 = LpVariable("BeefPercent", 0,None, LpInteger)

# The five constraints are entered
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100 * x1 + 0.200 * x2 >= 8.0, "ProteinRequirement"
prob += 0.080 * x1 + 0.100 * x2 >= 6.0, "FatRequirement"
prob += 0.001 * x1 + 0.005 * x2 <= 2.0, "FibreRequirement"
prob += 0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(prob.objective))