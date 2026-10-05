#MATPLOTLIB
"""
It is a python packahe that is used in data visualization to view data in a more grapgical format.
"""
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

height = np.random.normal(158,5.0,40)
weight = np.random.normal(58,8.0,40)

print("Height list:" + str(height))
print("Weight list:" + str(weight))


#plt.plot(weight,height)
#plt.show()

#NB in order to round off the values, use numpys round function(np.round) and not the normal one.

years = np.round(np.random.normal(2010,1,10),0)
population = np.round(np.random.normal(1.5,0.5,10),4)

print("Years list:" + str(years))
print("Population list:" + str(population))

populations = [40,43,45,44,60]
year = [2009,2010,2011,2012,2013]

plt.plot(year,populations)
plt.show()

plt.scatter(year,populations)
plt.show()



