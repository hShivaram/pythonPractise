# Description : Printing different patterns is a very good exercise to reinforce iteration through loops and strong
# logic building. Here you will be given a positive integer and you will generate pattern based on that integer.

# sample Output
#     *
#    *_*
#   *_*_*
#  *_*_*_*
# *_*_*_*_*

# please take input here
n = int(input())

# start writing your code here
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i - 1):
        print("*_", end="")
    print("*")
