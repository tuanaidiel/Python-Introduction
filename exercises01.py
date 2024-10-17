# Reverse the given number 98765
# the expected output 56789

original = 98765
reversed = 0
reversed = original % 10

original = original // 10
reversed = reversed * 10 + (original % 10)

original = original // 10
reversed = reversed * 10 + (original % 10)

original = original //10
reversed = reversed * 10 + (original % 10)

original = original // 10
reversed = reversed * 10 + (original % 10)

print(original)
print(reversed)

print ("----------------------------------------------------------")

# in loop
original = 98765
reversed = 0

while original > 0:
    reversed = reversed * 10 + (original % 10)  # Add the last digit of x to y
    original = original // 10            # Remove the last digit from x

print("original:", original)
print("reversed:", reversed)  