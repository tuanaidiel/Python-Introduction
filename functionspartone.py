# followed by block of code

def sayHelloWorld():
    print ("Hello World!!!")

sayHelloWorld()    #how to call a function
sayHelloWorld()
sayHelloWorld()

print ("----------------------------------------------------------")

# function definition
def greeting (name):
    print ("Good morning " + str (name)); 

# function caller
greeting ("David") # David is the argument
# note: number of argument must match the number of parameters
greeting ("Peter")

def simpleInterest (principle, period, rate):
    interest = (principle * period * rate) / 100
    print (interest)

# caller has access to principle, period,rate
#however no way for the caller to know the interest amount
simpleInterest (1000, 1, 6)
simpleInterest (1000, 2, 5)
print (simpleInterest (1000, 2, 5)) #not returning any value

print ("----------------------------------------------------------")

def calculatesimpleinterest (principle, period,rate):
    interest = (principle * period * rate) / 100
    return interest

print ("Interest amounnt:", calculatesimpleinterest (1000, 1, 6))
print ("Interest amounnt:", calculatesimpleinterest (1000, 1, 6))

interestamount = calculatesimpleinterest (2000, 1, 6)
print ("Principle amount:", 2000)
print ("Year:", 1)
print ("Rate:", 6)
print ("Interest amount:", interestamount)

print ("----------------------------------------------------------")

from userinput import keyboardInput    #from another file

mynumber = keyboardInput ("Enter a number:", int, "Number must be integer")
print ("square of mynumber: ", mynumber * mynumber)

print ("----------------------------------------------------------")

def calculateSI (principle, period=1, rate=6):
    interest = (principle * period * rate) / 100
    return interest

print (calculateSI (1000)) #default 1 and 6 is taken
print (calculateSI (1000,2)) #2 overwrite 1
print (calculateSI (1000,2,7)) #2 overwrite 1, 7 overwrite 6

print (calculateSI (principle = 1000, rate = 7))
print (calculateSI (principle = 1000, rate = 6))

print ("----------------------------------------------------------")

def total (mynumbers):
    result = 0
    for mynumber in mynumbers:
        result = result + mynumber

    return result

print (total ([10,20,30,40,50,60,70]))
print (total ([10,20,30,40]))
print (total ([10,20,30,40,50,60,70,80,90,100]))

print ("----------------------------------------------------------")

def calculatetotal (*mynumbers):  # (*) convert argument to list
    result = 0
    for mynumber in mynumbers:
        result = result + mynumber

    return result

print (calculatetotal (10,20,30,40,50,60,70))
print (calculatetotal (10,20,30,40))
print (calculatetotal (10,20,30,40,50,60,70,80,90,100))

print ("----------------------------------------------------------")

def plotgraph (graphtype, colors, *data):
    print ("graph type:", graphtype)
    print ("colors:", colors)
    print ("data:", data)

plotgraph ("boxplot", ["white", "black"], 10,20,30,40,50,60)

print ("----------------------------------------------------------")

def calculateTotalAverage(*data): #function definition
    total = 0
    for value in data:
        total = total + value
    average = total / len (data)

    return total, average # python will automatically convert them to tuple

result = calculateTotalAverage(10, 20, 30, 40, 50, 60, 70, 80)
print(result[0], result [1])

totalvalue, average = calculateTotalAverage (10, 20, 30, 40, 50, 60, 70, 80)
print(totalvalue, average)

print ("----------------------------------------------------------")

def printdetails(**arguments):
    print(arguments)

printdetails(firstname = "David", lastname = "John")