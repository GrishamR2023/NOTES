import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("MOCK_DATA.csv",header=0)
'''
states = []
for i in data["state"]:
    if not(i in states):
        states.append(i)


states = data.state.unique()
states.sort()
print(states)
'''
depTotal = []
deps = []
deps = data.department.unique()
deps.sort()
for dep in deps:
    total = 0
    costData = data.loc[data.department == dep,"cost"]
    for p in costData:
        total += p
    depTotal.append((dep,round(total,2)))
    
    
totals = []
for tup in depTotal:
    totals.append(tup[1])
totals.sort()
minVals = totals[:5]
maxVals = totals[-5:]
print(minVals)
print(maxVals)
minDeps = []
for val in minVals:
    for tup in depTotal:
        if val == tup[1]:
            minDeps.append(tup[0])
            
maxDeps = []
for val in maxVals:
    for tup in depTotal:
        if val == tup[1]:
            maxDeps.append(tup[0])
            


plt.bar(minDeps,minVals)
plt.ylim(1800000,2000000)
plt.ylabel("Sales")
plt.xlabel("Department")
plt.title("Bottom 5 sales per million")
plt.show()
plt.bar(maxDeps,maxVals)
plt.ylim(2100000,2300000)
plt.ylabel("Sales")
plt.xlabel("Department")
plt.title("Top 5 sales per million")
plt.show()