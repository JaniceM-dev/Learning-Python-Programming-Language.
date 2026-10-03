# 2**3 = 2^3

print(2**3)
# the function "type(num)" checks the datatype of a variable.

#Python Datatypes
"""
Datatypes in python include: 
int - integers or whole numbers
float - real numbers or fraction numbers
str - Strings or text
boolean - True or False
"""
#You can express a string eith both single and double quotes. ("" or '')
#in Boolean datatype capita;ization (True , False) is important.

"""
The operators you use such as '+' depends on the datatypes used. For example
2+3 = 5
"ab" + "cd" = "abcd"
"""
#Variable assignment in Python.
"""
The value to the right is given the name or inserted to the value in the left. Donot Forget this.
For Example:
new_savings + savings = total_savings --Wrong syntax.
totalsavings = new_savings + savings.
syntax is "VariableName = Value"  
"""
#Lists in Python
"""
Lists are used in order to give many values the same name/ a collection of related values.
The values in the list can be f the same or diff datatype as below.
fam1 = ["janice", "Dad","Mom","Shiku"]
fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23]

A list can also contain lists inside as below.
fam3 = [["janice",19],["Dad",55] ,["Mom",50],["Shiku",23]]

#1.Accessing Value in a list (list subsetting)
in order to access values in a list,we use indexing like in arrays. We have two methods of indexing
1.0-indexing
Here you read the indexes from 0.
fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23] - Their indexes:
(0,1,2,3,4,5,6,7)
fam2[0] = "Janice"

2.Negative indexing
Here we begin from the last value i.e index 7. The last value is given an index of -1.
fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23] - Their indexes:
(-8,-7,-6,-5,-4,-3,-2,-1)
fam2[-8] = "Janice"


fam2[0] = fam2[-8] = "Janice"

#2.List Slicing.
List Slicing refers to the process of selecting more than one value in a list.
This is done by using a colon ":"
The syntax is.
listName = [startingIndex(inclusive): LastIndex(exclusive)]
The above syntax creates a new list with only the selected range of values.
In the above, first value in the starting index is included in the range while the last value/index is not inclusive.
For Example:

fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23]
fam2 = [2:4]  
Output: ["Dad",55] . Here "Mom" which is in index 4 is not included hence is exclusive.

fam2 = [:4]
Output: ["janice",19, "Dad",55] - This prints out all the values before index 4 but does not include index 4.

fam3 = [4:] 
Output: ["Mom",50,"Shiku",23] - This prints all the values after index 4 (index 4 inclusive) upto the last value in the list it being inclusive as well.

When slicing using negative indexing remember that for example -2 is greater than -5 hence in the list below:
fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23]
fam2[-4:-2] - Output = ["Mom",50] - You slice in the direction of the normal list not that of negative indexing. ie: from left to right.

When accesing values in lists that are inside other lists ie:
fam3 = [["janice",19],["Dad",55] ,["Mom",50],["Shiku",23]]
In indexing you use the format:
listName = [index of bigger list][index of the smaller list]

fam3 = [1][0] 
Output = ["Dad"]

fam3 = [-1][1]
Output = 23

#3.List Manipulation.
1. Changing values in a list
1.1. Changing one value
fam2 = ["janice",19, "Dad",55,"Mom",50,"Shiku",23]
fam2 [0] = "Muthoni"
Output: fam2 = ["Muthoni",19, "Dad",55,"Mom",50,"Shiku",23]

1.2. Changing Multiple Values.
fam2 [2:4] = "Daddy",56
Output: ["janice",19, "Daddy",56,"Mom",50,"Shiku",23]
The above changes all values that are in that given range excluding the last Value.

2. Adding CValues in a list.
fam2 = fam2 + ["Adrian", 10]
Output:fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,"Adrian", 10]
This adds the new values at the end of the list.


#3. Deleting values from a list
Here we use the keyword del.For Example:
del fam2[-2:] 
Output:fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,]
This deletes the last two values in the list.
Dnot forget to add the name of the list after the keyword del befor the square brackets.

"""
fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,"Adrian", 10]
del fam2[-2:]

print(fam2)

"""
#Addressing in Lists.

when we say that: x = ["janice",19, "Dad",55,"Mom",50,"Shiku",23]
Here x contains the address of where the list is stored and not the list itself.
So if we say
x = y
we mean that we copy the address in x to y, so they are both pointing to the same list.
so when we say: y [-1] = 24
The list X  is also affected since they both point to the same list in  memory.
To ensure that the variable Y points to a different list with the same values as the list x then we can use:
1. y = list(x) - This uses the list function to mean create a new list that copies or has the exact same values as list x.
2. y = x[:] - This means create a new list y that has all the values in list x inclusive.

When you do the above, whatever change is made in the list y does not affect the list x.
"""

#FUNCTIONS IN PYTHON
"""
#Examples of Pythons Built in Functions.
1.max()
max(fam1)- This function checks the maximum value in the list.

2.round(value to be rounded,number of decimal places)
For example: round(1.456,2)
Output: 1.46 - The value is rounded off to two decimal places.
When you pass it off as one parameter it automatically rounds off the number to the nearest whole number.
For example:
round(1.456)
Output: 1

3.help() 
help function is used when you want to find information about a given in-built function or something in python.
For Example help(round) - gives info about the round function.
in Ipython shell specifically, this can also be done by placing a ? before the function name.
For example: ?round - here you DONOT put the brackets after the name of the function. 
This function is used in the .py file and the output is produced in the terminal or command prompt.

4.len()
len function helps in determining the length of a given range of values, characters e.t.c
For example:
len(fam2) - This determines the length of the list fam2.
Output will be: 8

5. int(),bool() str() and float() are all used when you want to change a value from one datatype to another.

6. pow(base,exp,mod)
the function pow() takes in three parameters:
base, exp and mod for modulus where modulus is optional.
an example is 2^3 %(modulus) 6 
2 - base
3 - exp
6 - modulus
The output of this is 8 modulus 6 which is 2.

7.sorted(iterable,key,reverse = ?(either true or false))
iterable = The values (for example a list) that you want to sort.
key(optional)- A custom key function can be used to customize the key order. 
reverse - Determines in which order it is being sorted
1.Reverse = none/ no reverse parameter given - It will automatically sort in ascending order.
2.reverse = FALSE - It sorts in ascending Order.
3. reverse = TRUE - It sorts in descending order.
For example: 
fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,]
sorted(fam2, reverse = FALSE) - This prints in ascending order.

in the documentation: sorted(iterable, /, *, key=None, reverse=False)
"/" symbol means that iterable is just a placeholder and cannot be used in function calling but should be replaced with the actual value.
Allowed: sorted([3, 1, 2])
Error: sorted(iterable=[3, 1, 2]) (Python will throw a TypeError)

"*" symbol shows that the key and reverse keywords must be used as they are with their keyword names and they cannot be replaced.
sorted([3, 1, 2], reverse=True)
Error: sorted([3, 1, 2], None, True) (Python won't let you pass True positionally for reverse)
"""

#METHODS IN PYTHON.
"""
methods are functions that are used in various python objects based on their types.
 Python objects can include: a list, an integer, a string e.t.c (everything in python is an object, and each object has a method depending on its datatype.)
 the syntax is: object.method()
   eg. fam2.index()
 Examples of methods of different datatypes.
 1.Lists
 1.1 index() -This method is used in lists to determine the index of a given value in a list. 
fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,]
For example: fam2.index("Daddy")
Output = 2
1.2 append() - This is used when you want to add more values to a list.
For Example: fam2.append("Adrian", 10) adds the new values to the list hence the new list becomes: 
fam2 = ["janice",19, "Daddy",56,"Mom",50,"Shiku",23,"Adrian", 10]
**YOU CAN ONLY APPEND/ADD ONE VALUE AT A TIME(THIS FUNCTION ONLY TAKES IN ONE PARAMETER AT A TIME.)


1.3 count() -This is used to determine the number of times a value has been used in a list.
for Example : fam2.count("Shiku")
Output: 1 -The string "Shiku" has only been used once in the list.

1.4 .remove(), that removes the first element of a list that matches the input, 

1.5 .reverse(), that reverses the order of the elements in the list it is called on.

2.Strings
You can use help(str) function to show you the diff methods you can use / that are associated with the string datatype.
Example of a string: name = "janice"
Methods.
1.1 capitalize()- This capitalizes the first letter of a string.
name.capitalize().
Output: name = "Janice" - The first letter is capitlized.

1.2 index(), This returns the index of a letter in a string.
Example: name.index("a")
Output:1

1.3 replace() - This method replaces a letter in a string with another. 
For Example: name.replace("e","a") - it replaces the letter e with a in the name "janice"
Output: name = "janica"

1.4 upper() - writes all the values in the string in uppercase.
eg: name.upper()
output: JANICE



"""
help(str)

#PACKAGES IN PYTHON
"""
A packages is like a diretory of python scripts in python where each script is a module.
Each  module specifys functions, methods and types aimed at solving specific problems. 
An example is 
1.numpy(numeric python) which is a package that helps to efficiently work with arrays.
2.Matplotlib which is used for data visualization.
3. Scikit-learn which is used for machine learning.

In order to use packages in your python scripts you need to install them.
The steps for installation are:
1.Go to the url :  https://pip.pypa.io/en/stable/Installation/                      
2. Download get-pip.py 
3. In your terminal type the command "python3 get-pip.py" to specify that it is a python3 version that we are using.
4. Now you can use the commands in the terminal "pip3 install numpy" for example to install the numpy package in your code.

In order to use the package in your code, you have to tell your python scripts that you want to use the package.
You can do this in two ways.
1.Importing te whole package.
1. At the top of the python script file type:
"import numpy" - This shows that we want to use this package in this specific script.
for example in your code:
  wrong- array([1,2,3,4,5]) - This will not work. You have to specify that it is from the numpy package.
  correct - numpy.array([1,2,3,4,5]) - This function takes in the elements of the list as inputs of the array.

2.Import it with an alias name that you will use throughout your code.
"import numpy as np"
for example in your code: 
  np.array([1,2,3,4,5])

2. Import only a specific module in the package 
1. Import only a specific module in the package that you want to use.(not mostly preferable for cleaner and more understandable code.)
"from numpy import arrays"
Now everytime you use the arrays function you are refering to the imported function.
For example in your code: array([1,2,3,4,5]) - Here you never repeat the name of the package,just the imported item.
np.array([1,2,3,4,5]) is more cleaner and understandable than array([1,2,3,4,5])

Example.
"import math"
In your code: you use math.pi when you need to use pi which is 3.14 instead of calculating it mannualy.
2**4 = 2 power 4 whch is 16
area of a circle = math.pi * 2 ** 4
area = pi *radius *radius. 
"""

#NUMPY
"""
It is difficult to perform ceratain operations in lists such as finding  the sum of each elemnt in two fifferent lists or performing operations on twoo different lists.
Hence here is where numpy package comes in. 
Using its array function, one can perform calculations indexwise for two different lists.
For example after installing the package using pip3 install numpy:
import numpy as np

height = [6.14,4.50,5.50,6.20]
weight = [64.50,65.30,55.70,54.40]

bmi = weight/height**2
An error will occur in the above statement as python's lists donot allow these calculations and operations on lists.

In order to allow manipulation, we use numpy.

np_weight = np.array([weight])
np_height = np.array([height])

bmi = np_weight/np_height**2
Output: bmi = [1.71089348 3.22469136 1.84132231 1.41519251] - A list containing the bmi calculated from each pair of elements in the two arrays.

##Numpy's arrays can only take in values of the same datatype. If you feed it a list with different datatypes they will all be converted to string datatype.
Numpy is like a different datatype like float and int. Hence it has different methods which behave differently. An example is addition in lists and addition in numpy. 
Also similar operations on different datatypes are different.

In lists:
num = [1,2,3]
num = num + num
Output:[1,2,3,1,2,3]  

In numpy:
np_num = np.array([1,2,3])
np_num = np_num + np_num
Ouptput: [2,4,6]

##Numpy adds the individual values in each index of the two arrays.

##Numpy Subsetting

#In subsetting numpy arrays, one can just use normal indexing.
For Example: bmi[1]
Output: 3.22 - It outputs the bmi calculated using index 1 of the two lists.

#When you want to output values of a specific criteria or condition.
Example. 
print (bmi > 20)
- It outputs a boolean of each index showing whether each value in the array has met that critera or condition.
[False False False False]

You can use the same list subsetting to produce a list where the values inside are only those that have met the condition.
Example:
print(bmi>3) 
#Output: [False  True False False]

print(bmi[bmi>3])
#Output : [3.22469136]

when you search for the type of a numpy array, the output is: 
type(np_height) 
numpy.ndarray
It shows that it is a type that was defined in the numpy package ad that it is an n dimentional array.

"""
# MULTI-DIMENTIONAL ARRAYS.
"""
Are arrays with more than one dimention eg, 3 sublists in one list. 3D array.
"""
# 2 DIMENTIONAL NUMPY ARRAYS.
"""
A 2-dimensional array doesn't mean "2 rows" or "2 columns." The "2" refers to the number of indices you need to locate one element. You need two numbers: one for the row and one for the column.
A 2D array can have any number of rows and any number of columns.
3D array: three indices, like a stack of tables: arr[layer][row][col].
They can be created from a list that is made ip of two sublists or more. 
Example: 
height = [6.14,4.50,5.50,6.20]
weight = [64.50,65.30,55.70,54.40]

np_2d = np.array([[height],[weight]])
you can use the attribute arrayname.shape to show the number of rows and columns in te array.
Example: np_2d.shape 
Output: (2,4) - 2 rows 4 columns.
NB: Atrributes are not similar to calling attributes in normal python objects.In objects methods we add brackets after them but in attributes we donot.
For example in the string object name.capitaize()
in numpy attributes : nd_2d.shape - no brackets.
2d numpy arrays follow the same rules as one dimentional where they can only have one datatype.

#SUBSETTING IN 2D ARRAYS
1.np_2d[0][1] - Output: 6.14
2.np_2d[0,1] - 0 for the row, 1 for the column.
3.np_2d [:,1:3] - the first : shows that we want to select both rows.
                - After the comma, it now shows the subsetting of the colums whose data we want. 1:3, we want for the first and second columns(in terms of indexing) and not the third.
                - Output: [[ 4.5  5.5]
                           [65.3 55.7]]
4. nd_2d [1,:] - The second row only and all the columns. 
For a  multi dimentional array with more than one row.
numpy.arrayname[row,column] eg: np_4d[3,5] - Row 3 column 5

NB:The concept of using commas for slicing is only understood in the numpy arrays and not in a normal list. In normal lists it will throw an error hence we only use colons ads they cn only be accesed in one dimention.
 example: baseball[0][1:5] - The first row and column 1 to 4 not 5.
So always make sure that when indexing using commas you are working on a numpy array and not on a normal list.  

#OPERATIONS ON 2D ARRAYS.
Addition: You can add a 2d array with another 2D arrays so that the addition takes place indexwise.
Multiplication: In order to multiply values in a 2D,you create another array with the same number of columns or the same number , with the values that you want to multiply each column with.
Example:
height = [6.14,4.50,5.50,6.20]
weight = [64.50,65.30,55.70,54.40]

np_2d = np.array([height,weight])
conversion = np.array([[0.0254],[0.453592]])
print(np_2d*conversion)
Output: 
[[ 0.155956   0.1143     0.1397     0.15748  ]
 [29.256684  29.6195576 25.2650744 24.6754048]]
"""
#NUMPY STATISTICS.
"""
Functions for Data Operations.
Syntax: np.function(arrayname)
Examples of functions.
1.np.mean(np_2d[0,:]) - This outputs the mean height or average height of all the heights.
2.np.mediun(np_2d[0,:]) - The outputs the mediun height after sorting from short to tall.(Height is in index 0.)
3.np.corrcoef(np_2d[0,:],np_2d[1,:]) - Correlation Cooeficient Checks whether height and weight are correlated. 
Example output
[[ 1.        -0.4671716]
 [-0.4671716  1.       ]]

Interpretation.
Diagonal (1.0): each variable correlates perfectly with itself.
Off-diagonal (about -0.47): the correlation between height and weight.
Explanation.
A correlation of -0.47 is a moderate negative relationship. 
In this data, taller people tend to weigh less.
 Look at the numbers: the tallest values (6.14, 6.20) go with the lowest weights (64.50 for 6.14, 54.40 for 6.20), 
 while the shortest height (4.50) goes with a high weight (65.30).
 It's not a strong or consistent pattern, which is why it's only around -0.5 rather than close to -1.
#NB:
#THESE FUNCTIONS BELOW ALL GIVE THE SAME OUTPUT.
print(np.corrcoef(np_2d[0,:],np_2d[1,:]))
print(np.corrcoef(height,weight))- Takes in the variables as inputs and finds their correlation.
print(np.corrcoef(np_2d)) - Takes the sublists as inputs and finds their correlation.


4.np.std(np_2d[0,:]) - Looks fr the standard deviation of the height. 
5.np.sum(np_2d[0,:])
6.np.sort(np_2d)
NB: The sum and sort functions are found in normal python but it is faster using numpys arrays since they support only one datatype.
"""
#GENERATING RANDOM DATA IN NUMPY
"""
Functions used :

1.np.ramdom.normal(mean,standard deviation,size/number of samples to be generated) 
Explanation.
This creates the given number of samples which are around the given mean and which have a spreadness of the standard deviation from the mean.
Most of the values fall around that deviation from the mean.


2. np.round(array,decimals) - eg np.round(height,2)
- This rounds off every value created in the array to a specific number of decimal places.

3.np.column_stack()
This takes 1D arrays and places them side by side and makes them the colums of a new 2D array.
Example: np.column_stack((height,weight))
The double parenthesis (height,weight) shows that the tuple we are forming has the height and weight values.

4. np.vstack()
It takes the two created arrays as the rows of the new 2d array.
np_total2dB = np.vstack((Height,Weight))
Eventhough we have the comma and the double parenthesis,it still creates the two as two different rows for the 2d array with the 40 values in each row as the columns.
Here the number of values in each array should be the same.

5. An alternative of this is making them a 2d array using the normal numpy array function.
np_total2dB = np.array([Height,Weight])

example 1: Height = np.round(np.randon.normal(1.75,0.20,5000),2) 
example 2: Weight = np.round(np.randon.normal(60.32,15,5000),2)
The functions above sample 2 random distributions 5000 times.
These create the height and weight arrays. 
np_total_random = np.column_stack((height,weight)) 
This creates a 2D array with 5000 rows and two height and weight columns in each row. 

The function above always runs different values all the time.
In order to ensure that the same results are given always, run the code/function 
np.random.seed(123) before you run the function np.ramdom.normal().
"""