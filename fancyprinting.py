#
product = "television"
quantity = 10
price = 1400.50
isAvailable = True

result = "I bought %s today. Total number: %d Per Price: %f" % (product, quantity, price)
print (result)

result = "I bought %s today. Total number: %d Per Price: %.2f" % (product, quantity, price)
print (result)

#
print ("----------------------------------------------------------")

result = f"{product:15s}{quantity:8d}{price:30.2f}"

print (result)
print (f"{product:15s}{quantity:8d}{price:20.2f}")
print (result)

print ("----------------------------------------------------------")

mynumbers = [2,4,6,8,10,12,14,16,18,20]
iseven = True

for mynumber in mynumbers:
    if (mynumber % 2 != 0): iseven = False
if (iseven):
    print ("All items are even numbers")
else:
    print ("Some items are not even numbers")

# 2nd condition
if all  ([(mynumber % 2 == 0) for mynumber in mynumbers]):
    print ("All items are even numbers")
else:
    print ("Some items are not even numbers")

print ("----------------------------------------------------------")

#swap values
x = 20
y = 50

temp = x
x = y
y = temp

print (x, y)