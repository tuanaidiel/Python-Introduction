class Student:
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def sayfullname(self):
        return self.firstname + " " + self.lastname

class Graduate(Student):

    def __init__ (self, firstname, lastname, graduatedyear):
        self.firstname = firstname
        self.lastname = lastname
        self.graduatedyear = graduatedyear

    def sayfullname(self):
        return super().sayfullname() + " " + str(self.graduatedyear)
    
    def __str__ (self): 
        content = "First Name: " + self.firstname + "\n"
        content += "Last Name: " + self.lastname + "\n"
        content += "Graduated Year: " + str(self.graduatedyear)
        return content


khairi = Student("Khairi", "Abu Bakar")
peter = Graduate("Peter", "Parker", 2023)
print (peter.sayfullname())
print (peter)

print (map (int, ["10", "20", "30"]))

