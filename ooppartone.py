class Patient:

    # (__init__) will get executed whenever a new object is created
    def __init__(self):
        print ("Object created successfully") 
        self.firstname = ""
        self.lastname = ""
        self.icnumber = ""
        self.medicineprices = []
        self.appointmentdate = ""
        self.appointmenttime = ""

    # another method
    def info(self):
        print ("First Name:", self.firstname)
        print ("Last Name:", self.lastname)
        print ("IC Number:", self.icnumber) 
        print ("Appointment Date:", self.appointmentdate)
        print ("Appointment Time:", self.appointmenttime)

    # method is returning value
    def doPayment(self):
        total = 25
        for price in self.medicineprices:
            total = total + price
        return total
    
    # method is taking more than 1 parameter
    def doAppointment(self, strdate, strtime):
        self.appointmentdate = strdate
        self.appointmenttime = strtime 


# first object
peter = Patient()
print (type(peter)) 

print("-------------------------------------------------------")

# second object
khairi = Patient()

# object with values
peter.firstname = "Peter"
peter.lastname = "Parker"
peter.icnumber = 998877
peter.medicineprices = [6.20, 12.80, 7.10]

# state in memory so it can print anytime
peter.doAppointment ("13-08-2024", "6:15PM")
peter.info()
print ("Amount to be paid:", peter.doPayment())

khairi.info()
print ("Amount to be paid:", khairi.doPayment())

# class list:
# def append (self, x) :
#   pass
# def extend(self, y) :
#   pass


# fruits = list (["apple", "orange","mango"])
# python give us the flexibility, through which we can create list without use the class list
# fruits = ["apple","orange","mango"]