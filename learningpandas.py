import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dict = {
"Country":["Kenya","Uganda","Tanzania","Zimbambwe","Malawi"],
"Capital":["Nairobi","Kampala","Da-el-Salaam","Harare","Lilongwe"],
"Population":[40.56,50.79,70.46,44.39,56.54],
"Area":[11.54,18.39,7.90,5.78,3.59]
}

dataTable = pd.DataFrame(dict)
dataTable.index = ["KE","UG","TZ","ZM","ML"]
print(dataTable)

print(dataTable ['Country'])
print(type(dataTable ['Country']))
print(dataTable [['Country']] )
print(type(dataTable [['Country']] ))
print(dataTable[1:4])

#USING LOC FUNCTION
print(dataTable.loc['KE'])
print(dataTable.loc[['KE']])
print(dataTable.loc[["KE","UG"]])
print(dataTable.loc[["KE","TZ","UG"],["Country","Capital"]])
print(dataTable.loc[:,['Country','Capital']])

#USING ILOC FUNCTION(INDEX)
print(dataTable.iloc[[0,1]])
print(dataTable.iloc[:,[0,1]])
print(dataTable.iloc [[0,1],[0,1]])

#print(dataTable[[0]]) - This does not work as in order to access a row, you can only use slicing and one bracket.
# print(dataTable [['UG']] ) - You cannot use an index to access a row.
#print(dataTable.loc[['Country']]) - When you use loc and iloc, the strict format is row values/indexes and then columns.You cannot give a column label in the place of a row.
csvData = pd.read_csv('assets\csvFiles\sample-sales.csv' , index_col= None, parse_dates = ['date'] , dtype= {'order_id':str},nrows = 10 )

#print(csvData)
#csvData.info()

print(dataTable['Population'] )
filteredData = dataTable['Population'] > 45
print(filteredData)
print(dataTable[filteredData])

print(dataTable[['Population','Area']])
filteredData2 = np.logical_and(dataTable['Population'] > 45,dataTable['Area'] > 10)
print(filteredData2)
print(dataTable[filteredData2])
print(dataTable[np.logical_and(dataTable['Population'] > 45,dataTable['Area'] > 10)])

for i,country in enumerate(dataTable["Country"]):
    print(i,country)

#print(dataTable.iterrows(dataTable[["Country"]]))

print("=========\n")
for index , item in dataTable.iterrows():
    print (index,item ['Country'], item['Population'])

print("=========\n")
for i ,(index,item) in enumerate(dataTable.iterrows()):
    print(i,index,item["Country"],item["Population"])


for row in dataTable.itertuples():
    print(row.Index, row.Country, row.Population)



for i, row in enumerate(dataTable.itertuples()):
    print(i,row.Index, row.Country, row.Population)

