"""
Avoid calling your file the same name as the name of the package you are installing.This will cause an error as instead of importing the required libraries, it imports the libraries of your local file which donot exist. 
To avoid this, give your files unique names .Avoid naming your scripts after libraries you plan to use. Common traps include numpy.py, pandas.py, random.py, math.py, test.py and requests.py. A quick check: if you can import the name, don't use it as a filename.
"""

import numpy as np
import math

height = [6.14,4.50,5.50,6.20]
weight = [64.50,65.30,55.70,54.40]

#bmi = weight/ (height**2) - Produces an error.

np_weight = np.array(weight)
np_height = np.array(height)


bmi = np_weight/np_height**2
print("BMI = " + str(bmi))

print("BMI = " + str(round(bmi[1],2)))

area = math.pi *3**4
print("Area = "+ str(round(area,2)))

total = height + weight #This extends the list by adding the weight values as extra list values of height.
np_total = np_height + np_weight #This adds the values in each index of each list.

print("List Summation =" + str(total))
print("Numpy Summation =" + str(np_total))
print(bmi > 20) #- It outputs a boolean of each index showing whether each value in the array has met that critera or condition.
#[False False False False]
print(bmi>3) 
#Output: [False  True False False]
print("Condition = True :" + str(bmi[bmi>3]))
#Output : [3.22469136]

#2DIMENTIONAL NUMPY ARRAYS
np_2d = np.array([height,weight])
#NB donot mmake the mistake of adding square brackets to a variable that was already a list.
#For example : np_2d = np.array([[height],[weight]]) -This is wrong
# np_2d = np.array([height,weight]) - This is correct
print(type(np_2d))
print(np_2d.shape)

print(np_2d[0][1])
print(np_2d[0,1])
print(np_2d[:,1:3])
print(np_2d [1,:])

conversion = np.array([[0.0254],[0.453592]])
print(np_2d*conversion)

#THESE FUNCTIONS BELOW ALL GIVE THE SAME OUTPUT.
print(np.corrcoef(np_2d[0,:],np_2d[1,:]))
print(np.corrcoef(height,weight))
print(np.corrcoef(np_2d))

print("Standard Deviation = " + str(np.std(np_2d[0,:])))
print("Sum of values in both rows = " + str(np.sum(np_2d[0,:])))
print("Sored values in each row = " + str(np.sort(np_2d)))

np.random.seed(123) # Makes the randomly created data constant(does not change each time the function is run).
Height = np.round(np.random.normal(150,10.5,40),2)
Weight = np.round(np.random.normal(58,5.5,40),2)

print("Random Height" + str(Height))
print("Random Height" + str(Weight))

np_total2dA = np.column_stack((Height,Weight))
np_total2dB = np.vstack((Height,Weight))
print("Total Random (column) = " + str(np_total2dA))
print("Total Random (row) = " + str(np_total2dB))

#Using 2B (2 rows,40 columns)
bmi2dB = np_total2dB[0,:] / (np_total2dB[1,:]**2)
print("Total 2D BMI OF DATA 2B = " + str(bmi2dB))


print("Mean Height of Random data 2B:" + str(round(np.mean(np_total2dB[0,:]),2)))
print("Std of Height of Random data 2B :" + str(round(np.std(np_total2dB[0,:]),2)))
print("Sorted Random data 2B:" + str(np.sort(np_total2dB)))

print("Mean Weight of Random data 2B:" + str(round(np.mean(np_total2dB[1,:]),2)))
print("Std of Weight of Random data 2B :" + str(round(np.std(np_total2dB[1,:]),2)))
print("Correlation coeeficient of data 2B:" + str(np.corrcoef(np_total2dB[0,:],np_total2dB[1,:])))

#Using 2A (40 rows,2columns)
bmi2dA = np_total2dA[:,0] / (np_total2dA[:,1]**2)
print("Total 2D BMI OF DATA 2A = " + str(bmi2dA))


print("Mean Height of Random data 2A:" + str(round(np.mean(np_total2dA[:,0]),2)))
print("Std of Height of Random data 2A:" + str(round(np.std(np_total2dA[:,0]),2)))
print("Sorted Random data 2A:" + str(np.sort(np_total2dA)))

print("Mean Weight of Random data 2A:" + str(round(np.mean(np_total2dA[:,1]),2)))
print("Std of Weight of Random data 2A:" + str(round(np.std(np_total2dA[:,1]),2)))


print("Correlation coeeficient of data 2A:" + str(np.corrcoef(np_total2dA[:,0],np_total2dA[:,1])))
