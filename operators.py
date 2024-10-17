# basic operators
x = 100
y = 200
print (x + y)
print (x - y)
print (x * y)
print (x / y)

# 2 more
x =7
y =3
print("Quotient:", x // y)
print("Remainder:", x % y)

x=2
y=3
print (x ** y)

# decimal
# 4.2 ceil 5
# 4.9 floor 4
# 4.2 round 4
# 4.5 round 5

# assignment operator
x = 10
x,y,z = 10,11,12
print (x,y,z)
# x,y,z = 10 ------------------- error

# step up
step = 0
step = step + 1
step = step + 1

# step down
step = 0
step = step - 1
step = step - 1

# steps (long legs) ------ there is high chance this guy to miss the floor
step = 0
step = step + 2
step = step + 2

# other
step += 1 # step = step + 1 or y+y=1
step += 2 # step = step + 2

step -= 1
step -= 2

step *= 1
step *= 2

step /= 1
step //= 1
step %= 1
step **= 1

x=10
y=15
z=10
print(x < y)
print(y > x)
print(x != y)
print(x == z)
print(x <= y)
print(y <= z)
print(y >= x)