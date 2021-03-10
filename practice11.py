import ast

input_str = input()
input_list = ast.literal_eval(input_str)

lis = []
# Write your code here

input_list.sort()
print(input_list[-2])
set1 = set(input_list)
print("set", set1)
lis = list(set1)
lis.sort()
print(lis[-2])

