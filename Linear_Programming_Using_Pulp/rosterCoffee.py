#https://towardsdatascience.com/how-to-solve-a-staff-scheduling-problem-with-python-63ae50435ba4

import gdown
import pandas as pd

from pulp import *

url = "https://drive.google.com/uc?id=15BPH7-3GGWBfXPJQ3stkT6SHQECbT-pt"
output = "shifts.csv"
#gdown.download(url, output, quiet=False)

df = pd.read_csv("shifts.csv", index_col=0)

df = df.fillna(0).applymap(lambda x: 1 if x == "X" else x)


a = df.drop(index=["Wage rate per 9h shift ($)"], columns=["Workers Required"]).values


# number of shifts
n = a.shape[1]

# number of time windows
T = a.shape[0]

# number of workers required per time window
d = df["Workers Required"].values

# wage rate per shift
w = df.loc["Wage rate per 9h shift ($)", :].values.astype(int)


y = LpVariable.dicts("num_workers", list(range(n)), lowBound=0, cat="Integer")


# Create problem
prob = LpProblem("scheduling_workers", LpMinimize)

#print(list(range(n)),[w[j] * y[j] for j in range(n)])

prob += lpSum([w[j] * y[j] for j in range(n)])

print(a)
for t in range(T):
    prob += lpSum([a[t, j] * y[j] for j in range(n)]) >= d[t]
    print([a[t, j] * y[j] for j in range(n)],d[t])

#print([a[t, j] * y[j] for j in range(n)])

prob.solve()
print("Status:", LpStatus[prob.status])

for shift in range(n):
    print(
        f"The number of workers needed for shift {shift} is {int(y[shift].value())} workers"
    )







