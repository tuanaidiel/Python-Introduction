# Find the largest digit in 78693

x = 78693
y = 0

if(x % 10 >= y):
    y = x % 10     #x=78693

x = x // 10
if(x % 10 >= y):
    y = x % 10     #x=7869

x = x // 10
if(x % 10 >= y):
    y = x % 10     #x=786

x = x // 10
if(x % 10 >= y):
    y = x % 10     #x=78

x = x // 10
if(x % 10 >= y):
    y = x % 10     #x=7

print("The largest number in 78693 is:", y)
print("x:", x)

