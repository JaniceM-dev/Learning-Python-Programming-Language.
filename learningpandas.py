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

csvData = pd.read_csv('assets\csvFiles\sample-sales.csv' , index_col= None, parse_dates = ['date'] , dtype= {'order_id':str},nrows = 10 )

print(csvData)
csvData.info()

