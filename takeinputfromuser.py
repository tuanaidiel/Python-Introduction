yourname = input("What is your name: ")
print("Hello ", yourname, ", Good morning", sep="")

print("Data type of the input is always string:", type(yourname))

principle = float(input("Enter amount (RM): "))
period = float(input("Enter the year: "))
rate = float(input("Enter Rate (%): "))
interest = (principle * period * rate) / 100
print("Interest amount:", interest)
print("Total amount to be paid:", principle + interest)