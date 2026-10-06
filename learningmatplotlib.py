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

"""
#plt.loglog() - Both scales become logarithic.
plt.xscale('log')
plt.xlabel('Logarithimic Scale')
plt.ylabel('Normal Scale')
plt.scatter(weight,height)
plt.title('Scatter Plot')
#plt.show()
#plt.clf()
"""


#NB in order to round off the values, use numpys round function(np.round) and not the normal one.

years = np.round(np.random.normal(2010,1,10),0)
population = np.round(np.random.normal(1.5,0.5,10),4)

print("Years list:" + str(years))
print("Population list:" + str(population))

populations = [40,43,45,44,60]
numbers = [10,3,6,7,9]
year = [2009,2010,2011,2012,2013]

"""
#plt.plot(year,populations,'s')
#plt.show()


#plt.scatter(year,populations)
#plt.show()
help(plt.hist)

"""
plt.hist(populations,bins=4,label='Histogram of Population 1',bottom=2,edgecolor = 'black',color='brown',range=(40,50),linewidth = 2,orientation='horizontal'
         )

plt.hist([populations,numbers],bins=4,label=['Histogram of Population 2','Histogram of Numbers'],bottom=2,edgecolor = ['green','Purple'],color=['yellow','pink'],linewidth = 3,orientation='horizontal'
         )
plt.legend()
plt.show()