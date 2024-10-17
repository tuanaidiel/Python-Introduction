# Relationship

class Address:
    def __init__ (self, street_one, city, postcode, state, country):
        self.street_one = street_one
        self.city = city
        self.postcode = postcode
        self.state = state
        self.country = country


class Customer:
    def __init__ (self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber 
        self.addresses = []

class VipCustomer (Customer):
    def __init__ (self, firstname, lastname, icnumber, discount):
        super(). __init__ (firstname, lastname, icnumber)
        self.discount = discount 
        self.addresses = []


# VIP is child, Customer is parent
# Customer object created automatically when VipCustomer object is created
peter = Customer ("Peter", "Parker", 998877)

addressone = Address("15 Lorong", "Petaling", 8888, "Selangor", "Malaysia")
peter.addresses.append (addressone)

addresstwo = Address ("20 Lorong", "Segamat", 7777, "Selangor", "Malaysia")
peter.addresses.append (addresstwo) 

aida = VipCustomer("Aidawaty", "Abdullah", 112233, 10)

print (type (peter))
print (type (aida))











