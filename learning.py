
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
They can be created from a list that is made up of two sublists or more. 
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

NB:The concept of using commas for slicing is only understood in the numpy arrays and not in a normal list. In normal lists it will throw an error hence we only use colons as they can only be accesed in one dimention.
 example: baseball[0][1:5] - The first row and column 1 to 4 not 5.
So always make sure that when indexing using commas you are working on a numpy array and not on a normal list.  

#OPERATIONS ON 2D ARRAYS.
Addition: You can add a 2d array with another 2D arrays so that the addition takes place indexwise.
Multiplication: In order to multiply values in a 2D,you create another array with the same number of columns or the same number , with the values that you want to multiply each row with.
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

#MATPLOTLIB
"""
It is a python package that is used in data visualization to view data in a more graphical format.

You first begin by installing the Matplotlib packge by typing:
pip3 install matplotlib

NB: matplotlib uses numpys arrays for data visualization hence installing matplotlibs package automaticaly imports numpy if it was not available already.
But installing numpy package does not mean that the matplotlib package is installed automatically. Hence when you use this approach, you have to install matplotlib as well.

#import matplotlib.pyplot as plt - This involes importing the subpackage pyplot from matplotlib and it is imported and used throughout as plt
"""
#Working with matplotlib
"""
plt.plot(height,weight) - Used to plot a line graph with the parameters shown.
The first one in the brackets is the horizontal axis while the second one is the vertical axis.
In order to determine how the points should appear in the output graph, we use markers. Examples are:
1.plt.plot(x, y, 'o-') - The o draws a circle marker around each data point and the '-' means draw a straight line between each data point.

2.plt.plot(x, y, 'r--') - means draw a red dashed line.

3.plt.plot(x, y, 's') - used for square markers only.

4.plt.scatter(x,y, s=[list]) - IT shows that the size oeach plot/point is equal to specific values maybe of another list.This only works in a scatter plot as this is the only one we use points.

5.plt.scatter(x,y, c=col) - c=col shows that the colors of each of the points are to be given based on a seperate list col that is a list with all the colours corresponding to each value in the plot. Should have the same number of values as the values in both the lists forming the x and y axis.

6. plt.scatter(x,y, alpha = 0.8) - Shows the transparency of each dot. When 0 it is almost transparent,when 1 it is fully visible.

7. plt.text(x, y, 'the text') - It is used when you want to label specific points in the grapgh. It mean that you label 'the text' where the value of x is x and the value of y is y.
For example: plt.text(1550, 71, 'India')
             plt.text(2500, 80 , 'China')
8.plt.grid() - It is used to draw gridlines on the graph.


plt.scatter() - Used to draw a scatter plot plotting only the points and not drawing a line along them.

plt.show() - You must run this in order to show the created graph.

plt.show() displays a plot; plt.clf() cleans it up again so you can start afresh with a new histogram.

Always call the functions to customize the graph such as to label the axis before you call plt.show().
plt.xscale() - This sets the scale of the x-axis.

plt.xscale('linear') - The default.
plt.xscale('log') -  The converts the values that you have in the x axis (horizontal axis) to logarithimic values.For example the ranges span in multiples of 10 ie. 1,10,100,1000,10000,100000.
plt.xscale('symlog') - Used to do the same as plt.xscale('log') but it handles both negative and positive values correctly.
plt.xscale('logit') - Values must be strictly between 0 and 1.
Exactly 0 or 1 gives an infinite logit, and values outside that range are undefined, so those points won't be drawn.
On a linear axis, 0.001, 0.01 and 0.1 would bunch up near the left edge, and 0.9, 0.99 and 0.999 near the right. On the logit scale, they spread out symmetrically around 0.5, so the points appear evenly spaced.

plt.yscale('log') for the y-axis,
plt.loglog() for both, 
and plt.semilogx() / plt.semilogy() as shortcuts for plotting with one log axis.


plt.xlabel('log scale') 
xlabel: adds a text label under the x-axis (log scale).
Mentioning "log scale" tells readers the axis isn't linear.
(plt.ylabel(...) does the same for the y-axis.)
plt.title('Scatter Plot') - Gives the graph a title.

plt.yticks() - Used to define the ranges of values in the y axis.For Example:

plt.yticks([0,2,4,6,8,10]) - The y axis has this range of values starting from 0.
ply.yticks([0,2,4,6,8,10],
           [0B,2B,4B,68,8B,10B]) - This is used to rename the values above to the values in the second list for example to show that the values are in billions. Ensure that the ranges are the same.              )
Line graphs are mostly useful when you have time values in the x axis but in other cases it is more useful and important to use a scatter plot and you can convert the values in the x axis to be exponential(log).


#HISTOGRAM
The height of the histogram shows how many datapoints are in a given range.

We use:
plt.hist()
Parameters passed in the hist function for the histogram.

In a list passed in a histogram, 
the y axis = the number of values in the list.
the x axis = the range of values / the values in the list.
                                
1. plt.hist(ages, bins=6)- Shows that the list we are using is the ages list and that we want the values to be divided in  ranges of 6 hence 6 bins.
If you donot specify this, the histogram will be drawn with bins of 10.

2. plt.hist(ages, bins=6, density=True)  - Density involves calculating a frequency dencity of each height ensuring that the area of each bar is always 1. This ensures that all height are subsidised incase the values have  very large heights.

3.plt.hist(ages, bins=6, weights=none / weights = purchases) - Here purchases is a seperate list that contains the weights of each value eg the amount spent by each customer.
Here there are two grapgh at each bin, one for the normal count which is the normal values and the other with the weights where eacg value is added with its weight.

4.plt.hist(ages, bins=6, cumulative=True) - Here the frequency is a cummulative frequency where the height of each bin = its height + the heights of all its previous bins.

5.plt.hist([ages_a, ages_b], bins=6) - Used when you are passsing in two datasets. The datasets appear side by side in each bin.

6.plt.hist([ages_a, ages_b], bins=6 stacked=True) - Used when you want the values in the two lists to stack on top of each other in each height. The total height is the sum of the heights of each of the two datasets in each bin.

7.plt.hist(ages, bins=6, range=(20, 50)) - This specifies the range meaning that every value outside the range is not counted.

8.plt.hist(ages, bins=6, histtype='bar') - This shows the type/drawing style of the histogram.
a) bar - Bars for each bin.
b) step - Draws an outline at each height level and there are no bars to seperate bins.
c) stepfilled - It uses step but adds colour to the regions below the line.

9.plt.hist(ages, bins=6, orientation='vertical'/orientation='horizontal') - Defines the orientation of the histogram. Default is vertical.

10. plt.hist(ages, bins=6, rwidth=None /rwidth=0.5) - Shows the thickness of each bar in the bin. Ranges berween 0 and 1. When it is 1 there are no spaces between bars.

11. plt.hist(ages, bins=6, align='mid'/align='right'/align='left') - Shows how the bars are aligned based on the right or left edges of each bin. Mostly used when rwidth is below 1.

12.plt.hist(ages, bins=6, log=True) - This makes the height axis(y axis) to be logarithimic.

13.plt.hist(ages, bins=6,bottom=None) - This is used to set the height with which each bin starts from,whether it starts from the bottom 0 or from a specific height value above the bottom eg 2.5.

14.plt.hist(ages, bins=6, color='#2a78d6') - This sets the colour of the bargraphs to a specific color.

15.plt.hist(ages, bins=6, label=None/label=['A', 'B']{for two datasets}) - This used to give labels to each axis. In order to display the legends you have to call plt.legend().

16.plt.hist('age', data=df) - This is used when you have data in a table and only want to refer to one column in the table and draw a histogram of it.

17. The symbol  * - Means that every parameter after it must be written with its name, eg data=df not just df.

18. The symbol **kwargs - Means anything else that can be used eg to style the bars as desired.

19. edgecolor='black' - This means that the colours of the edges of each bin/bar are of a specific color.

20.alpha=0.5 - Transparency from 0 to 1.

21.linewidth=2. - Linewidth of each edge bar.

Example: 
plt.hist([ages_a, ages_b], bins=6, range=(10, 70),
         histtype='bar', rwidth=0.8, stacked=True,
         color=['steelblue', 'orange'], label=['A', 'B'],
         edgecolor='black', alpha=0.8)
plt.legend()
plt.show()

"""
#DICTIONARIES.
"""
Dictionaries store values in terms of key value pairs. In order to access a value you just pass in the key as a parameter.
Example Syntax:
dictionary name = {"Key":Value}
world = {"Kenya":50.6,"Uganda":40.69,"Tanzania":30.34}
world["Kenya"] = 50.6
world.keys() - It is a method for dictionaries that is used to determine all the keys that are found in the dictionary.

In dictionaries, keys have to be immutable objects. Immutable objects are objects whose values cannot be changed after they have been created
Examples of immutable objects are datatypes of string,integer,float and boolean. All these are acceptable as keys.
However,a list is not acceptable as its value can change after it is created. It is muttable.

world = {0:30,"Kenya":50.6,True:70,30.5:40.9} - These are all acceptable.
world = {["Janice",20,159]:30} - Not acceptable as the value of a list can be changed once created.

#Adding values in a dictionary.
In order to add values in a dictionary, you follow the same syntax as if you are searching for a key but instead you assighn it a value.

example: world ["Malawi"] = 57.90
world =  {"Kenya":50.6,"Uganda":40.69,"Tanzania":30.34,"Malawi":57.90}

#Searching for a key in a dict
To identify whether a key is in a dictionary: key in dictionary
For Example: "Malawi" in world.

#Updating a value in a dict.
Use the same syntax as for adding as python knows that that key already exists and that you are not trying to create another one. Every key is unique.
world["Kenya"] = 55.4
world =  {"Kenya":55.4,"Uganda":40.69,"Tanzania":30.34,"Malawi":57.90}

#deleting a key and its value in a dictionary
we use the del() function which is the same as in lists but here we specify only the key and the value is automatically deleted.
del(world["Malawi"])

#Lists vs Dictionaries.
You can use lists when you need to access large subsets of data.
Whereas you can use dictionaries when you need to search for data faster and where the data can be accesed by a unique key.

One can also create a dictionary where the corressponding values are also dictionaries.
Example:
world2 = {"Kenya":{"Capital":"Nairobi","Population":40.56},"Tanzania":{"Capital":"Da-el-salaam","Population":80.59}}
To access the capital city of tanzania.
world['Tanzania']['Capital']

"""
#PANDAS 
"""
PANDAS is a high level data manipulation tool that is used to manupulate data.
It was created by Wes Mkinney and is built on the numpy package.
It is more advanced than numpy.

In order to use it, one must first install it using pip3 install pandas
Then to import it in a file you use :
import pandas as pd

NB: python -c "import pandas; print(pandas.__version__)"
python - Runs the python interpreter
-c this tells python that we are running a command that we want it to execute otherwise it will expect a file to run.
"import pandas; print(pandas.__version__)" - The command we want it to run.
import pandas - Checks whether pandas has been installed otherwise it shows an error.
; - The semicolon shows that we are writting two seperate statements in one line.
print(pandas.__version__) - Prints pandas version if it exists. The underscores are part of the name. __version__ .

In certain conditions one may require to manipulate data in a table but it becomes difficult to use numpys 2D arrays when the data has different datatypes.
Here is where we use the pandas package specifically pandas dataframe to store values in a table.
In a table, The rows represent the data while the columns represent the variables.


#BUILDING DATAFRAMES
There are several ways to create and use dataframes.
1. Creating them manually using a dictionary.
This approach is not convenient expecially when you have large sets of data.

In order to build a a dataframe to accomodate the values of a table,you can start by using a dictionary.
Where the keys are the column labels while the values are a list of value /observations of each column.

For Example

dict = {
"Country":["Kenya","Uganda","Tanzania","Zimbambwe","Malawi"],
"Capital":["Nairobi","Kampala","Da-el-Salaam","Harare","Lilongwe"],
"Population":[40.56,50.79,70.46,44.39,56.54],
"Area":[11.54,18.39,7.90,5.78,3.59]
}

dataTable = pd.DataFrame(dict) -{DataFrame in sentence case} This creates a dataframe which is a table taking in the values from the dictionary.
.index - This is a dataframe attribute that is used to assign special names to each record thus preventing them from being autoincreamented per record.
It may be an attribite but we are assigning index values to each record ie row in the table. Hence we use an equal sign.
We assign a list of values for each row. The number of values in the list should be equal to the number of values/ records or rows in the table.
example : dataframename.index = [list of names]
dataTable.index = ["KE","UG","TZ","ZM","ML"] -

2.Importing Data from a csv file.
CSV means comma seperated values.
In order to import this data and view it as a dataframe you use the command:
data = pd.read_csv(path to the csv file)
.read_csv - This is an function to read a csv file.
There are so many parameters you can pass inside it to manipulate how your data is imported from the csv file. You can read the documentation.
1.data = pd.read_csv(path to the csv file,index.col = 0) - You set this when the imported table already has row labels but pandas still gives each row a new index.This parameter sets the index column to 0 so none.

Parameters 
a.Telling Pandas how the file is laid out
1.data = pd.read_csv(path to the csv file,sep = ';' or sep = '\t' (Tab Seperated) or sep = '|' ) - this is used to tell pandas how the file is laid out and the character that seperates the values.
We use this when the values are not seperated by commas.

2. pd.read_csv('data.csv', header=None) - Header is used to show which row holds the column names. Default header = 0(The first row.). 
Else when header = none, pandas gives default columun names of 0, 1 ,2 ...

3.pd.read_csv('data.csv', header=None , names = ['country','life_exp','population'] - This is paired with header = none and is used to allow you give the columns your own column names.

4.pd.read_csv('data.csv', encoding='latin-1') - Encoding is used to fix garbled characters.It is used when you see strange symbols or an error.

b. Choosing which data to load.
5. pd.read_csv('data.csv', usecols=['country','gdp']) - This is used when you want to selects specific columns to use.

6. pd.read_csv('data.csv', nrows=100) - nrows is used to load specific number of rows. Useful when peeking a large dataset.

7.pd.read_csv('data.csv', skiprows=3 (skips the first three rows.)/skiprows = [1,2] (This skips specific lines 1 and 2)) - Used to skip rows at the start or specific rows.
. Useful when the file has title lines or notes above the real table.

8. pd.read_csv('data.csv', skipfooter = 2 engine = 'python') - skipfooter is used to skip rows at the bottom such as total or notes lines. It requires engine = 'python' .

9. pd.read_csv('data.csv', index_col='country') - This determines which column forms the row labels, if none, you can provise your own which is tedious for a large dataset and reqiores index_col = 0.

c. Contrling Datatypes.

10. pd.read_csv('data.csv', dtype={'zip_code': str, 'age': 'int32'}) - Dtype : forces columns to be read as a specific type. This matters for things like ZIP codes
or IDs, where 00123 would otherwise lose its leading zeros by becoming the number 123. 

11. pd.read_csv('data.csv', parse_dates=['order_date'], dayfirst=True) -  converts text like 2026-10-10 into real date objects, so you can sort by time or extract months and years.
dayfirst=True - This is used when you want to sort the dates by day first.

12.d.read_csv('data.csv', thousands=',') - thousands and decimal: handle numbers formatted differently from the default. 1,200,000 can be read as a number.
pd.read_csv('data.csv', decimal=',', sep=';') - In european style, 3,14 can be read as 3.14 .

13.pd.read_csv('data.csv', converters={'price': lambda s: float(s.replace('$',''))}) - Converters helps one apply their own function to a column for example stripping a % sign etc. 
'price': lambda s: float(s.replace('%','')) :
'price' - This is the exact column name whose values you want to change.
lambda s: float(s.replace('$','')) - This shows the function you want to call on each column.
lambda s - This is a one line function used without a name and it used for short rules and def for longer ones.
float(s.replace('%','')) - This removes the % character and replaces it with nothing and converts the data to a float. This is useful for data that you want to convert to float for calculations.

You can also use:
converters = {'column_name': some_function}
converters = {'discount': clean_percent} - You write the function without the brackets after. Then you define the function elsewhere.

def clean_percent(s):
    return float(s.replace('%',''))
  
This does the same thing as the lamda's one line function.
This is very slow for large data, hence it is more advisable to load the data first and then clean it with column wide tools such as:
df['price'].str.replace('$', '', regex=False).astype(float).


d.Handling Missing Data.
14. pd.read_csv('data.csv', na_values=['N/A', '-', 'missing']) - na_values tells pandas which strings should count as missing data. In several messy files, null data is given entries such as N/A , - or missing . 

15. pd.read_csv('data.csv', comment='#') - comment ignores everything after a chosen character in a line. Useful for files with notes. 

16. pd.read_csv('data.csv', on_bad_lines='skip') - on_bad_lines: decides what to do with broken rows, for example a row with too many columns. The default raises an error. You can skip them instead.

5.Working with Large files.
for chunk in pd.read_csv('huge.csv', chunksize=100_000):
print(chunk.shape)       
# process each 100,000-row piece

chunksize: reads the file in pieces instead of all at once, so a file bigger than your memory can still be processed. It returns an iterator you loop over.
Combining usecols , dtype and nrows is also a good way to keep large files manageable.

f. Where the file comes from.
The first input does not have to be a file on your computer.
pd.read_csv('https://example.com/data.csv')   # straight from a web link
pd.read_csv('data.csv.gz')                    # compressed files work too

After importing, check the result with: 
df.head() (first 5 rows) and 
df.info() (column names, types and missing counts). This is the quickest way to see whether your parameters did what you intended.

dict = {
"Country":["Kenya","Uganda","Tanzania","Zimbambwe","Malawi"],
"Capital":["Nairobi","Kampala","Da-el-Salaam","Harare","Lilongwe"],
"Population":[40.56,50.79,70.46,44.39,56.54],
"Area":[11.54,18.39,7.90,5.78,3.59]
}
dataTable = pd.DataFrame(dict)

#SELCTING AND INDEXING DATA IN A DATAFRAME.

1. Selecting data in a specific column.
1. dataframename ['The column whose data you want to output.']
dataTable ['Country'] - If you look at the type of the output data, you will find that it is a series.
type(dataTable ['Country']) - Output: <class 'pandas.Series'>
A series is like a 1 dimentional array that can be labbeled. Many series make up a dataframe.
Inorder to ensure that the data in that column is output as a dataframe, we use two square brackets.
dataTable [['Country']] 
type(dataTable [['Country']]) - Output : <class 'pandas.DataFrame'>
To select more that one column : dataTable[['Country','Capital']]
NB: You can only select one column using this method as a series with one bracket pair. In order to select more than one column you select them as a dataframe with two bracket pairs. 
Plain square brackets can pick columns, or they can pick rows, but one pair of brackets can't pick both at once.

2. Selecting specific rows. Here we use index slicing.
You can only access rows by slicing and not giving one index as square brackets are only used to acces columns by their labels.
#print(dataTable[[0]]) - This does not work as in order to access a row, you can only use slicing and one bracket.
print(dataTable[0:1]) - Correct.

dataTable[1:4] - This selects rows 1, 2,3 but not 4. It also selects the column lables row.
NB: Donot use double brackets when handling rows, instead use single brackets since the output is already a dataframe.
 When using normal brackers to acces values, There is no specific order, but you cannot access rows using labels, only indexes .Label are for columns only.

 #LOC FUNCTION
 .loc is a pandas function that is used to select items and to slice pandas dataframe based on labels.
When you use it,it is similar to subsetting 2d numpy arrays.
Here rows are accesed by labels and not indexes.
Rows are accesed with labels only in loc NOT using brackets only..

 For Example:
dataTable.loc['KE'] 
Output :
Country         Kenya
Capital       Nairobi
Population      40.56
Area            11.54
Name: KE, dtype: object

Using double brackets makes it a dataframe, in form of a table:
print(dataTable.loc[['KE']])
Output:
 Country  Capital  Population   Area
KE   Kenya  Nairobi       40.56  11.54

Selecting more than one row:
dataTable.loc [['KE','UG']] - Use double square brackes for a dataframe.

In order to slect specific rows and specific columns,the syntax is
dataTable.loc[[list of row labels],[list of columns]]
dataTable [['KE','UK','UG'],['Country','Capital']] - Selects only those specific rows and columns.
dataTable [:,['Country','Capital']] - You use the colon when you want to select all the rows but specific columns.
You only select the rows when you want to display all the columns as done in the first example.


#ILOC FUNCTION
.iloc - This is a pandas function that is used to select rows and columns based on indexes.
For example: 
dataTable.iloc [[row indexes],[column indexes]]
dataTable.iloc [[0,1]]
Output:
Country  Capital  Population   Area
KE   Kenya  Nairobi       40.56  11.54
UG  Uganda  Kampala       50.79  18.39

Selecting specific rows and columns.
print(dataTable.iloc [[0,1],[0,1]])
  Country  Capital
KE   Kenya  Nairobi
UG  Uganda  Kampala


To select all rows and specific columns,we use:
dataTable.iloc [:[0,1]]
Output:
 Country       Capital
KE      Kenya       Nairobi
UG     Uganda       Kampala
TZ   Tanzania  Da-el-Salaam
ZM  Zimbambwe        Harare
ML     Malawi      Lilongwe

NB: #print(dataTable.loc[['Country']]) - This is wrong.
When you use loc and iloc, the strict format is row values/indexes and then columns.
You cannot give a column label in the place of a row.
It is only in iloc where we use indexes with double brackets, we donot do that in normal indexing.

#print(dataTable[[0]]) - This does not work as in order to access a row, you can only use slicing and one pair of square brackets.
#print(dataTable[0:1]) - Correct
# print(dataTable [['UG']] ) - You cannot use an index to access a row if you are not using the loc function.

"""
#COMPARISON OPERATORES
"""
Comparison only happens between values or objects of the same datatype. You cannot compare a string and an integer.
Float and int works.
int and numpy array with integer values works.

Comparison Operators.
> - Greater Than
< - Less Than
<= - Less than or equal to.
>= - Greate than or equal to.
!= - Not equal to

Comparison in strings compares character by character starting with the first one in their alphabetical order.
#BOOLEAN OPERATORS AND OR NOT
AND - True if both are true
OR - True if either are true
NOT - Negates the current result.
This does not work for numpy arrays. 
The equivalents for this are numpy functions:

1.np.logical_and()
2.np.logical_or()
3.np.logical_not()

Example: 
height = [6.14,4.50,5.50,6.20])
weight = [64.50,65.30,55.70,54.40])

np_weight = np.array(weight)
np_height = np.array(height)

bmi = np_weight/np_height**2
Example 1:
bm1 > 2 and bmi < 3 - This produces an error

Example 2:
print(bmi>4)
Output:[False False False False]

Example 3:
print(np.logical_and(bmi>4,bmi<3))
Output: [False False False False]

Example4:
print(np.logical_or(bmi>4,bmi<1))
Output: [False False False False]

Example 5:
print(np.logical_not(bmi>4))
Output: [ True  True  True  True]

To output the values that have met that criteria, we pass the function inside square brackets.
print(bmi[np.logical_not(bmi>4)])
Output: [1.71089348 3.22469136 1.84132231 1.41519251]

"""
#CONTROL STRUCTURES
"""
Syntax:
if condtion:
  expression

There is a semicolon after the condition. If the condition is true the statement is executed  else it is not.
Ensure that there is a tab/4spaces under the if condition to show that all the statements underneath it are under the if condition and are only executed if the statement is true.

Overall Syntax:
if condtion:
  statement
elif condition:
  statement
else:
  statement

To get out of the loop,you simply ensure that the next statement does not have a tab or space before it.
"""

#Subsetting Pandas Dataframes.
"""
Inorder to subset pandas dataframes, for exampke to get only values that have met a specific criteria, we use:
1.Get the column whose values you want to filter.
2.Carry out the condition, mening filter the values that have met the condition and store it in a variable.
3.Use those values as the index/input in square brackets of the whole data frame.
NB:In all these we use single brackets since we are working on a series not a dataframe in manipulation.
For Example:

dict = {
"Country":["Kenya","Uganda","Tanzania","Zimbambwe","Malawi"],
"Capital":["Nairobi","Kampala","Da-el-Salaam","Harare","Lilongwe"],
"Population":[40.56,50.79,70.46,44.39,56.54],
"Area":[11.54,18.39,7.90,5.78,3.59]
}

dataTable = pd.DataFrame(dict)

we want to see only the rows whose population is greater than 45.
Step 1:
dataTable['Population'] 
Output:
KE    40.56
UG    50.79
TZ    70.46
ZM    44.39
ML    56.54
Step 2:
filteredData = dataTable['Population'] > 45
Output:
KE    False
UG     True
TZ     True
ZM    False
ML     True
Name: Population, dtype: bool
Step 3:
dataTable[filteredData]
Output:
 Country       Capital  Population   Area
UG    Uganda       Kampala       50.79  18.39
TZ  Tanzania  Da-el-Salaam       70.46   7.90
ML    Malawi      Lilongwe       56.54   3.59

This has the same output as: 
dataTable[dataTable['Population'] > 45]

#Using The boolean Conditions,and or not.
We want to find values with a population greater than 45 and an area greater than 10.
Here we use the three functions:
np.logical_and()
np.logical_or()
np.logical_not()
Since pandas is an extension of numpy.
Step 1:
dataTable[['Population','Area']]
Output:
 Population   Area
KE       40.56  11.54
UG       50.79  18.39
TZ       70.46   7.90
ZM       44.39   5.78
ML       56.54   3.59
Step 2:
filteredData2 = np.logical_and(dataTable['Population'] > 45,dataTable['Area'] > 10)
Output:
KE    False
UG     True
TZ    False
ZM    False
ML    False
Step 3:
dataTable[filteredData2]
Output:
 Country  Capital  Population   Area
UG  Uganda  Kampala       50.79  18.39

This produces the same output as:
dataTable[np.logical_and(dataTable['Population'] > 45,dataTable['Area'] > 10)]

"""