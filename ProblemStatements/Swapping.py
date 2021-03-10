# Description
# You are given two integer variables,  x and y. You have to swap the values stored in x and y.

# Take input using input()

# input() takes input in form of the string
in_string = input()

# here extract the two numbers from the string
my_list = in_string.split(',')
x = int(my_list[0])
y = int(my_list[1])

# print x and y before swapping
print("x before swapping: {0}".format(x))
print("y before swapping: {0}".format(y))

# Writing your swapping code here
x = x + y
y = x - y
x = x - y

# print x and y after swapping
print()
print("x after swapping: {0}".format(x))
print("y after swapping: {0}".format(y))
