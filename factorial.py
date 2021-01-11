# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    # base case
    if n == 0:
        return 1
    #recursive case 
    else:
        return n * factorial(n -1)
    # Write code here
    pass

print(factorial(5))
# => 120