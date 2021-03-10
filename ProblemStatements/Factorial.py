# Description
# Factorial is a mathematical function denoted by '!'. It is defined as

# n factorial = n!= 1*2*3...*(n-1)*n

# In this question, you have to make a function that will take an integer as input, and return the factorial of that
# integer if that integer is greater than or equal to zero and return -1 if the number is less than zero or negative.

# Note: the function doesn't return print the factorial but returns it.

# take the input here
number = int(input())


# the function definition starts here
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        z = 1
        for i in range(1, n + 1):
            z = z * i
        return z
    # write the function here that finds and RETURNS factorial of next


# function definition ends here

# do not alter the code typed below
k = factorial(number)
print(k)
