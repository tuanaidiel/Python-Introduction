# recursive function

givennumber=5
factorial = 1

for currentnumber in range (5,0,-1):
    factorial = factorial * currentnumber
print ("Factorial of", givennumber, "is", factorial)

# mathematically
# n * (n-1) * (n-2) * (n-3) * (n-4) 
# n * (n-1) * (n-2) * ..... (n-(n-1)) 
# n * (n-1)! 
# 5 * 4!

# 97432
# 2 * 10000 + reverse(9743)
# 2 * 10000 + 3 * 1000 + reverse (974)


inputnumber = int(input("Input a number: "))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial (n-1)
    
print("Factorial of", inputnumber, "is", factorial(4)) 

print ("--------------------------------------------------------")

# sum of digits

givennumber=97409

def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits (n // 10)

print("Sum of digits for", givennumber, "is", sumofdigits(97409))


