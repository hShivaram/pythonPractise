# Description
# You have to find and print the smallest element of the list given as input.

# input have been taken for you here
import ast

input_str = input()
input_list = ast.literal_eval(input_str)

# start writing your code here
m = input_list[0]

for item in input_list:
    if item < m:
        m = item
print(m)
