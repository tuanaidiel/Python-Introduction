def sayHello(user):     #receive address location where the David object is
    print("Good Morning", user)

name = "David"
sayHello(name)      #passsing address location, not David where David is 

def greeting():
    print ("Welcome")

def startSpeech(x):   # x is address
    x()               # python will go to the address and try to execute

startSpeech (greeting) #passing function as an argument to another function

print ("----------------------------------------------------------")

def authenticate (username, password):
    def simpleInterest(principle, period, rate):       #inner function
        interest = (principle, period, rate) / 100  
        return interest
    
# inner function can be called from outer funtion

    if (username == 'admin' and password == 'pwd123'): 
        interest = simpleInterest (1000, 1,6)
        return interest
    else:
        return None 
    
print (authenticate("admin", "pwd123"))

print ("----------------------------------------------------------")

def authorize (username, password):
    def simpleInterest(principle, period, rate):       
        interest = (principle, period, rate) / 100  
        return interest

    if (username == 'admin' and password == 'pwd123'): 
        return simpleInterest
        
    else:
        return None 
    
result = authorize ("admin", "pwd123")
print (result(1000, 2, 5)) 

print (authorize ("admin", "pwd123")(2000, 3, 4))
