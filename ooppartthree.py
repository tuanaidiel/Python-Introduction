# encapsulation

# khairi.firstname = "something" 
# cannot modified outside the class when use (.__)
# value cannot be assigned to the property
# because the property becomes private

class Patient:
    def __init__(self, firstname, lastname, icnumber):
        print ("Object created successfully") 
        self.__firstname = firstname
        self.__lastname = lastname
        self.__icnumber = icnumber

    def getFirstName (self):
        return self.__firstname 
    
    def setFirstName (self, firstname):
        illegalnames = ["", "something", "none", "null", "-"]
        if (firstname not in illegalnames):
            self.__firstname = firstname 

    # fake property
    # property is built in function
    firstname = property(getFirstName, setFirstName) 


    def info(self):
        print ("First Name:", self.__firstname)
        print ("Last Name:", self.__lastname)
        print ("IC Number:", self.__icnumber) 

peter = Patient ("Peter", "Parker", 998877)
peter.__firstname = "Something"
peter.info()

print ("--------------------------------------------------")

peter = Patient ("Peter", "Parker", 998877)

peter.setFirstName = "HEHEHEHE"
print("First Name:", peter.getFirstName())
peter.info() 
