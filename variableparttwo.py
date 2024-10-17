# multiple things to one variable
fruits = ["apple", "orange", "mango", "banana", "grapes"]
print (fruits)

print("-----------------------------------------------------")
fruits = ["apple", "orange", "mango", "banana", "grapes"]
print (fruits[0]) 
print (fruits[1]) 
print (fruits[2]) 
print (fruits[3]) 
print (fruits[4]) 

print("-----------------------------------------------------")
print (fruits[-1]) 
print (fruits[-2]) 
print (fruits[-3]) 
print (fruits[-4]) 
print (fruits[-5]) 

#range
#end index is not included
print("-----------------------------------------------------")
slice = fruits [1:5]
print(slice) 

slice = fruits [0:3]
print(slice) 

slice = fruits [4:5]
print(slice) 

slice = fruits [0:5:2]   #0+2+2
print(slice) 

slice = fruits [:4]    #start from 0
print(slice) 

slice = fruits [2:]    #start from to 2 to the last
print(slice) 

# negative index in range
# start index < last index
# not reverse
print("-----------------------------------------------------")
slice = fruits [-4:-1]
print (slice)

slice = fruits [-1:-5]   # error/not execute
print (slice)

slice = fruits [-1:-5:-1]   # -1, -1 + -1, -2 + -1, -3 + -1
print (slice)

slice = fruits [::-1]   # fully reverse
print (slice)

# len function also used to find the number of item in the list
print(len(fruits))

# string
print("-----------------------------------------------------")
message = "welcome to python programming"
print (message[11:17])

# list has different id
fruits = ["apple", "orange", "mango"]
newfruits = ["apple", "orange", "mango"]
print (id(fruits))
print (id(newfruits))

# not real copy
oldfruits = fruits
fruits[0] = "durian"
print (oldfruits)
print (fruits)

fruits = ["apple", "orange", "mango", "durian", "rambutan", "cempedak"]
localfruits = fruits [3:]
print (fruits)
print (localfruits)

#tuple use ()
print("-----------------------------------------------------")
countries = ("Malaysia", "Singapore", "Thailand", "Indonesia", "Vietnam")
print (countries)
print (countries[0])
print (countries[1])
print (countries[-2])
print (countries[1:4])

#sum ([10, 20, 30, 40, 50]) ----------- passing 1 argument
#sum (10, 20, 30 ,40, 50) ------------- passing 5 arguments

#sum((10, 20, 30, 40, 50)) ------------ tuple

print("-----------------------------------------------------")
countrieslist = list(countries)
print (countrieslist)
print (type(countrieslist))
countriestuple = tuple(countrieslist)
print (countriestuple)
print (type(countriestuple))

print (isinstance(countrieslist, list))

print("-----------------------------------------------------")
mynumber = [10]
print (mynumber, type(mynumber))

mynumber = (10,)
print (mynumber, type(mynumber))

# if a function call suppose to return tuple and one good day
# the function returns a single value then it becomes integer
# If you try to pull the items using [] (mynumber[0]) it will throw runtime error

# if (type(mynumbers)): # this wrong
#    print("This is tuple")

if (isinstance(mynumber, tuple)):
    print("This is tuple")

# unpack to individual variables
studentdetail = ["khairi", "abu bakar", 99887766, 3000]

firstname = studentdetail [0]
lastname = studentdetail [1]
icnumber = studentdetail [2]
fee = studentdetail [3]

print (firstname, lastname, icnumber, fee)

# but in python we do this
fname, lname, ic, amount = studentdetail
print (fname, lname, ic, amount)

seperator = ("=" * 80)
print (seperator)

studentdetails = [
    ("khairi", "abu bakar", 99887766, 3000),
    ("peter", "adam", 11111111, 4000),
    ("chan", "haris", 22222222, 5000),
]

print (studentdetails)

seperator = ("=" * 70)
print (seperator)

for studentdetail in studentdetails:
    print (studentdetail) #tuple

for fname, lname, ic, amount in studentdetails:
    print (fname, lname, ic, amount)

print ("-----------------------------------------------------------")

fruits = ["apple", "orange", "mango"]

fruits. append ("grapes")
fruits. extend (["durian", "rambutan"])

print (fruits) 

print ("-----------------------------------------------------------")
x = [10,20,30,40,50]
y = [60,70,80,90,100]
z = x + y
print (z) 

print ("-----------------------------------------------------------")

# insert is a method inside the list object
#fruits is a list object

print (fruits) 
fruits.insert (2, "banana")
print (fruits) 
fruits.insert (5, "pineapple")
print (fruits) 
fruits. remove ("mango") # delete a fruit
print (fruits)

del fruits [1] #del deletes anything from memory permanently
print (fruits)

del fruits #delete entire list

print ("-----------------------------------------------------------")

fruits = ["apple","orange","apple","mango","durian","rambutan","apple","cempedak"]
fruits.clear()   # output will be empty -----> []
print (fruits)

fruits = ["apple","orange","apple","mango","durian","rambutan","apple","cempedak"]
localfruits = fruits.copy () 
print (fruits)              # same
print (localfruits)         # same

fruits.append ("pineapple")
print (fruits)              # add pineapple
print (localfruits)         # same

print (fruits.count ("apple")) 
print (fruits.index ("durian")) 
print (fruits.index ("apple")) 

print (fruits)
fruits.pop ()           # remove the last item in the list
print (fruits)

fruits.sort ()          # sort it by ascending order (a,b,c)
print (fruits)          # loose original ordering, copy to maintain original

fruits.reverse ()       # 
print (fruits)

print ("-----------------------------------------------------------")

