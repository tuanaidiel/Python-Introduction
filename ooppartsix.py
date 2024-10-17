# Class

class Student:

    count = 0

    def __init__ (self):        # constructor method
        #properties
        self.firstname = ""     # instance variable
        self.lastname = ""      # firstname and lastname are initialized with 
                                # empty strings "" 

    def info(self):
        print (self.firstname)
        print (self.lastname)

# Objects

peter = Student ()              # class
#instance variables
peter.firstname = "Peter"
peter.lastname = "Parker"
peter.info()                    # instance method
Student.count += 1

khairi = Student()              # class
#instance variables
peter.firstname = "Parker"
peter.lastname = "Parker" 
khairi.info()                   # instance method  
Student.count += 1

print(Student.count)
 

