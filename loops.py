fruits = ["apple", "orange", "mango", "banana", "grapes"]
for fruit in fruits:
    print(fruit)

seperator = ("=" * 70)
print (seperator)

#print fruit for 6 letters
for fruit in fruits:
    if (len(fruit) == 6):
        print (fruit)

indexes = range (0, len(fruits))
print (indexes)
# we can typecast range object to list object
print (list (indexes))

for index in range (0, len(fruits)):
    print (index, fruits [index])

#another condition
for index in range (0, len(fruits)):
    print (index)

print ("-----------------------------------------------------")

print (enumerate (fruits))
print (list(enumerate(fruits)))

for index, value in enumerate (fruits):
    print (index, value)

print (list (range (0, 101, 25)))

print ("-----------------------------------------------------")

fruits = ["apple", "orange", "mango", "banana", "grapes"]
for fruit in fruits:

    if (fruit == "banana"): break
    print(fruit)
else:
    print ("All fruits printed successfully") 

print ("-----------------------------------------------------")

mynumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for mynumber in mynumbers:
    if mynumber % 2 == 0:
        print (mynumber)

print ("-----------------------------------------------------")

mynumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for mynumber in mynumbers:
    if mynumber % 2 == 0: continue
    print (mynumber)

print ("-----------------------------------------------------")

mynumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for mynumber in mynumbers:
    if mynumber % 2 != 0: continue
    print (mynumber)

print ("-----------------------------------------------------")

# while loop
# 1) used when not have a list
# 2) used when not know how many time to repeat
# 3) used when have condition to terminate

# for loop
# 1) used when know how many time to repeat

# exercise: reverse the number
givennumber = int (input ("Enter the number: "))
result = 0
while (givennumber > 0):
    result = (result * 10) + (givennumber % 10)
    givennumber = givennumber // 10

else:
    print (result) #this case guvennumber <= 0

print ("-----------------------------------------------------")

