
# Description You are planning to go to your friend's wedding and you have long events all month, lasting at least a
# few days. You have the start and end dates of events and your task is to find out events overlapping with the
# wedding date.
#
# The code for taking input has already been written for you, please don't modify that, but do read and try to
# understand the way input has been taken. You will be asked to take input on your own for most of the problems here
# onwards. Taking data in a suitable format is an important skill for a Data Scientist.


# taking input
import ast

input_str1 = input()
input_list1 = ast.literal_eval(input_str1)
events = input_list1

wedding = int(input())

count = 0
# start writing from here
for i in range(len(input_list1)):
    for j in range(len(input_list1[i]) - 1):
        if input_list1[i][j] <= wedding <= input_list1[i][j + 1]:
            count += 1

print(count)

