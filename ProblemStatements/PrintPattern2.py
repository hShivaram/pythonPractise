# Description
# Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern
#
# Sample Input: 5
#
# Sample Output :
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


import string

n = int(input())

# Write your code below
a = string.ascii_lowercase
List = []
for i in range(n):
    s = "-".join(a[i:n])
    # print(s)
    # print("slicing ",s[::-1],"one more slicing",s[1:])
    List.append(s[::-1] + s[1:])
# print(List)
width = len(List[0])

for i in range(n - 1, 0, -1):
    # print(i)
    print(List[i].center(width, "-"))

for i in range(n):
    print(List[i].center(width, "-"))
