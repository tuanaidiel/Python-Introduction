x = 10
print (x)

x = None
print (x)
x = "Television"

def sayHello ():
    message = "Hello"
    print (message)

    #x = "Radio"
    #print(x)

    global x

    x = "Radio"
    print (x) 

print(x)
sayHello()
print(x)

print ("Thank you")

print ("-------------------------------------------------------")

def outerfunction ():
    outer = "Parker"      #local variable belongs to outerfunction
    def innerfunction ():
        inner = "Peter"   #inner can be access inside innerfunction
        print (inner)

    #print(inner) #error
        print(outer)
        innerfunction ()

    #outer = "John"
    #print (outer)

        nonlocal outer
        outer = "John"
        print(outer) 

    print (outer)
    innerfunction()
    print(outer)

outerfunction()
