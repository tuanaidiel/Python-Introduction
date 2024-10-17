# lambda function is  nothing but anonymous function
# assigned to a variable

'''
# normal function
def sayHello():
    print ("Hello")

# anonymous function
def ():
print ("Hello")

# anonymous function assigned to a variable
sayHello = def():
print ("Hello")

'''

sayHello = lambda: print ("Hello")

sayHello ()

def square(x):
    return x ** 2

# bracket on parameter are not necessary
# retunr keyword also not necessary
square = lambda x: x ** 2

print (square(3))

print ("---------------------------------------------------")

def simpleinterest (principle, period, rate):
    return (principle * period * rate) / 100

print (simpleinterest (1000, 1, 6))

#2nd method
simpleinterest = lambda principle, period, rate: (principle * period * rate) / 100
print (simpleinterest (1000, 1, 6)) 
