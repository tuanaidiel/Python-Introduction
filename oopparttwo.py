class Patient:

    # we are modifying the constrcutor to take 3 compulsory parameters
    # assign parameter values to property directly
    def __init__(self, firstname, lastname, icnumber):
        print ("Object created successfully") 
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.medicineprices = []
        self.appointmentdate = ""
        self.appointmenttime = ""

    def info(self):
        print ("First Name:", self.firstname)
        print ("Last Name:", self.lastname)
        print ("IC Number:", self.icnumber) 
        print ("Appointment Date:", self.appointmentdate)
        print ("Appointment Time:", self.appointmenttime)

    def doPayment(self):
        total = 25
        for price in self.medicineprices:
            total = total + price
        return total
    
    def doAppointment(self, strdate, strtime):
        self.appointmentdate = strdate
        self.appointmenttime = strtime 

# object
# we should not let peter object to be created 
# without firstname, lastname, icnumber

peter = Patient("Peter", "Parker", 998877)   
peter.info()

print ("--------------------------------------------------")

khairi = Patient ("Khairi", "Abu Bakar", 776655)
khairi.info()

# encapsulation
khairi.firstname = "something"