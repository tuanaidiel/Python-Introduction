mynumbers = [10,20,30,40,50]

for mynumber in mynumbers:
    print (mynumber)

def addfive(n):
    return n + 5

mynumbersplusfive = map(addfive, mynumbers)

#map

for mynumber in mynumbersplusfive:
    print(mynumber)

print ("-----------------------------------------------------------")

fruits = ["apple", "orange", "mango", "durian", "television"]
colors = ["red", "orange", "yellow", "deep yellow"]
taste = ["sweeter", "sour", "sweeter", "sweeter"]
combination = zip(fruits, colors, taste) 

for item in combination:
    print(item)

#
mynumberiter = iter(mynumbers)
print (next(mynumberiter)) 
print (next(mynumberiter)) 
print (next(mynumberiter)) 
print (next(mynumberiter, None))   # None use to check if
print (next(mynumberiter))         # there is no more item 
print (next(mynumberiter, None))

print ("-----------------------------------------------------------")

# not necessary ----- better use for loop
hasnext = True
mynumberiter = iter(mynumbers)
while (hasnext):
    item = next(mynumberiter, None)

    if (item == None):
        hasnext = False
    
    else:
        print(item) 

print ("-----------------------------------------------------------")

def multiplesoffive():
    number = 0
    yield number
    number = number + 5
    yield number
    number = number + 5
    yield number
    number = number + 5
    yield number

for mynumber in multiplesoffive():
    print (mynumber)

print ("-----------------------------------------------------------")

myiterator = iter(multiplesoffive())

print (next(myiterator)) 
print (next(myiterator)) 
print (next(myiterator)) 
print (next(myiterator)) 

print ("-----------------------------------------------------------")

def multiplesofseven():
    number = 0
    yield number
    while (number < 70):
        number = number + 7
        yield number

for mynumber in multiplesofseven():
    print (mynumber)






