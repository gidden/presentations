#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

years = [2008,2030,2050,2100]
n = 1000
time = np.linspace(years[0],years[-1],n)

demand_points = [[372,600,1000,2500],
                 [372,700,1500,5000]]

slopes = [[],
          []]

for i in range(len(years)-1):
    denominator = float(years[i+1] - years[i])
    for j in range(len(demand_points)):
        numerator = float(demand_points[j][i+1] - demand_points[j][i])
        slopes[j].append(numerator/denominator)

demand = [[],
          []]
for entry in time:
    if entry <=years[1]: i = 0
    elif entry <=years[2]: i = 1
    else: i = 2
    for j in range(len(demand_points)):
        demand[j].append(demand_points[j][i] + (entry - years[i]) * slopes[j][i])

plt.plot(time,demand[1],label='High Demand')
plt.plot(time,demand[0],label='Moderate Demand')
plt.axis([min(time),max(time),0,max(demand[1])])
plt.legend(loc=2)
plt.title('Nuclear Energy Demand - INPRO BAU')
plt.xlabel('Year')
plt.ylabel('Demand (GWe)')
#plt.show()
plt.savefig('inpro-demand.eps') #
plt.clf()

        
