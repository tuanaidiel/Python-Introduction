class AtmCard:
    def __init__(self):
        print("ATM Card")

class CreditCard:
    def __init__(self):
        print("Credit Card")
    def info(self):
        print("Info: Credit Card")

class DebitCard:
    def __init__(self, accountholder):
        print("Debit Card")
        self.accountholder = accountholder
    def info(self):
        print("Info: Debit Card", self.accountholder)

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self, accountholder):
        super().__init__()
        DebitCard.__init__(self, accountholder)


mybankcard = BankCard("Khairi") # mybankcard is an instance of BankCard Class
mybankcard.info() # calling instance method info
DebitCard.info(mybankcard) # even though it looks like
# we are calling a class method, we are not calling class method
# we are calling instance method. 
# Calling instance method via Class 