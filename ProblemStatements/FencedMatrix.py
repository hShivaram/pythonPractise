# Description You will be given two positive integers m and n. You have to make a list of lists (which can be
# visualised as a matrix) of size m*n, that is m sublists (rows), with each sublists having n integers (columns). The
# matrix should be such that it should have 1 on the border and 0 everywhere else. See sample input and output for
# more clarification.
#
#
#
# ----------------------------------------------------------------------
#
# Input:
#
# Two integers separated by a comma
#
#
#
# Output:
#
# A list of lists of size m*n printed like matrix as shown in the sample output.

import ast

m_list = ast.literal_eval(input())

row = int(m_list[0])
col = int(m_list[1])

orginal_list = []
# start writing code here
for i in range(row):
    list = []
    for j in range(col):
        list.append(0)
    orginal_list.append(list)

# print(orginal_list)

for i in range(row):
    for j in range(col):
        if i == 0 or j == 0 or i == row - 1 or j == col - 1:
            orginal_list[i][j] = 1

for i in orginal_list:
    print(i)

