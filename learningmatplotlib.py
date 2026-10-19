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

populations = [40,43,45,48,60]
np_numbers = np.array([107,340,500,700,400])
np_numbers = np_numbers * 2
year = [2009,2010,2011,2012,2013]
col = ['blue','yellow','Brown','Purple','Grey']
countries = ['Kenya','India','Uganda','Tanzania','Angola']

plt.scatter(year,populations,s = np_numbers,c=col)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Graph of Population against Year')
plt.yticks([40,42,44,46,48,50,52,54,56,58,60,62],
           ['40K','42K','44K','46K','48K','50K','52K','54K','56K','58K','60K','62K'])
plt.xticks([2009,2010,2011,2012,2013])

for x,y,name in zip(year,populations,countries):
    plt.text(x,y,name)
#This is a loop that has been used to name the countries instead of naming them manually. Can only be used if the lists are similar and corresponding indexwise.

plt.grid(True)
#plt.show()


#plt.scatter(year,populations)
#plt.show()


"""
#help(plt.hist)
plt.hist(populations,bins=4,label='Histogram of Population 1',bottom=2,edgecolor = 'black',color='brown',range=(40,50),linewidth = 2,orientation='horizontal'
         )

plt.hist([populations,numbers],bins=4,label=['Histogram of Population 2','Histogram of Numbers'],bottom=2,edgecolor = ['green','Purple'],color=['yellow','pink'],linewidth = 3,orientation='horizontal'
         )
plt.legend()
plt.show()
"""

#DICTIONARIES
world = {"Kenya":50.6,"Uganda":40.69,"Tanzania":30.34}
print(world.keys())
print(world['Kenya'])
world['Tanzania'] = 40.50
print(world['Tanzania'])
world['Malawi'] = 60.50
print(world)
del(world['Malawi'])
print(world)


plt.scatter(year,populations)

for i , country in enumerate(countries):
    plt.text(year[i],populations[i],country)

plt.show()