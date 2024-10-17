# age < 10 is children
# age >=10 and <18 is minor
# age >=18 and <21 is tenager
# age >=21 and <60 is adult
# age >=60 and above is senior

#1st condition
x = int(input("Enter age: "))

if (0<x<10):
    print ("children")
else:
    if (18>x>=10):
        print ("minor")
    if (21>x>=18):
        print ("tenager")
    if (60>x>=21):
        print ("adult")
    if (x>=60):
        print ("senior")

#2nd condition
x = int(input("Enter age: "))

if (x>0 and x<10):
    print ("children")
elif (x>=10 and x<18):
        print ("minor")
elif (x>=18 and x<21):
        print ("tenager")
elif (x>=21 and x<60):
        print ("adult")
else:
    print ("senior")

#3rd condition
x = int(input("Enter age: "))

print("children") if (x<10) \
    else print ("minor") if (x >= 10 and x <18) \
    else print ("tenager") if (x >= 18 and x <21) \
    else print ("adult") if (x >= 21 and x <60) \
    else print ("senior")
