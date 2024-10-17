# process a list and get new list

celciusvalues = [0,1,2,3,4,5,6,7,8,9]
farenheitvalues = []

# farenheitvalues.append  (10)
# methods are nothing but function inside an object

for celciusvalue in celciusvalues:   #TRADITIONAL FOR LOOP
    farenheitvalues. append (celciusvalue * 9/5 + 32)

print (celciusvalues)
print (farenheitvalues)

# another case
print ("-------------------------------------------------------------") 

prices = [10,20,30,40,50,60,70,80,90]
sstprices = []

for price in prices:
    sstprices. append (price + (price * 0.06))

print (prices)
print (sstprices)

print ("-------------------------------------------------------------") 

fruits = ["apple", "orange", "mango"]
newfruits = []

for fruit in fruits:
    newfruits.append(fruit)

newfruits.append("rambutan")
print (fruits)
print (newfruits)

print ("-------------------------------------------------------------") 

fruits = ["apple", "orange", "mango"]
newfruits = [fruit for fruit in fruits] #list comprehenension
newfruits.append ("grapes")
print (fruits) 
print (newfruits)

print ("-------------------------------------------------------------") 

celciusvalues = [0,1,2,3,4,5,6,7,8,9]
farenheitvalues = [(celciusvalue * 9/5) + 32 for celciusvalue in celciusvalues]
print (celciusvalues)
print (farenheitvalues)

print ("-------------------------------------------------------------") 

prices = [10,20,30,40,50,60,70,80,90]
sstprices = [price + (price * 0.06) for price in prices]
# sstprices.append (100)
print (prices)
print (sstprices)

print ("-------------------------------------------------------------") 

fruits = ["apple", "orange", "mango"]
newfruits = [len(fruit) for fruit in fruits] #list comprehenension
print (fruits) 
print (newfruits)

print ("-------------------------------------------------------------") 

mynumbers = [1,2,3,4,5,6,7,8,9,10]
evennumbers = []

for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append(mynumber)

print (mynumbers)
print (evennumbers)

# second condition

mynumbers = [1,2,3,4,5,6,7,8,9,10]
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]

print (mynumbers)
print (evennumbers)

print ("-------------------------------------------------------------") 

shirtcolors = ["White", "Red", "Blue"]
pantcolors = ["Black", "Brown", "Blue"]
combinations = []

for shirtcolor in shirtcolors:
    for pantcolor in pantcolors:
        combinations.append ((shirtcolor, pantcolor))

print (combinations)

# second condition
combinations = [(shirtcolor, pantcolor) for shirtcolor in shirtcolors for pantcolor in pantcolors]
print (combinations) 

# third condition
shirtcolors = ["White", "Red", "Blue"]
pantcolors = ["Black", "Brown", "Blue"]
combinations = []

for shirtcolor in shirtcolors:
    for pantcolor in pantcolors:
        if (shirtcolor != pantcolor):
            combinations.append ((shirtcolor, pantcolor))

print (combinations)

# fourth condition
combinations = [(shirtcolor, pantcolor) for shirtcolor in shirtcolors for pantcolor in pantcolors if (shirtcolor != pantcolor)]
print (combinations) 

print ("-------------------------------------------------------------") 

#TRADITIONAL FOR LOOP
farenheitvalues = []
for celciusvalue in celciusvalues:   #TRADITIONAL FOR LOOP
    farenheitvalues. append (celciusvalue * 9/5 + 32)

#list comprehensive
farenheitvalues = [(celciusvalue * 9/5) + 32 for celciusvalue in celciusvalues]

#3rd method
def convertCelciusToFarenheit (celciusvalue):
    return (celciusvalue * 9/5) + 32
farenheitvalues = map(convertCelciusToFarenheit, celciusvalues)
print (list (farenheitvalues))

print ("-------------------------------------------------------------") 

# We process a list and we get a new list
# Overhere the number of items in the newly created list
# is less than or equals to the number of items in the original list
mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the even numbers only
evennumbers = []
for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append (mynumber)

# use list comprehension
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]
# this type of problems can be solved using built id function called filter
# You need to create a function that returns True or False

# Function that returns True or False is also called "Predicate function"
def isEven (number):
    return number % 2 == 0
evennumbers = filter (isEven, mynumbers)
print (list(evennumbers))

#next
from functools import reduce
mynumbers = [1,2,3,4,5]
def add (previousvalue, currentvalue):
    return previousvalue * currentvalue  # (+) initial 0, (*) initial 1
result = reduce (add, mynumbers, 2)
print ("result:", result)

print("------------------------------------------------------------")

listofnumbers = input("Key in numbers separated by comma")
mynumbers = listofnumbers.split (",") 
for mynumber in mynumbers:
    print(mynumber, type(mynumber))

intmynumbers = []
for mynumber in mynumbers:
    intmynumbers.append(int(mynumber))

for mynumber in intmynumbers:
    print(mynumber, type(mynumber))

print("------------------------------------------------------------")

#other method
intmynumbers = [int(mynumber) for mynumber in mynumbers]

print("------------------------------------------------------------")

#other method
intmynumbers = map(int, mynumbers)

for mynumber in intmynumbers:
    print(mynumber, type(mynumber))