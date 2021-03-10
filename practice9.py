import ast
import sys

input_str = input()
sides = ast.literal_eval(input_str)  # list of side lengths
print(sides)
if sides[0] > sides[len(sides) - 1]:
    block = sides[0]
else:
    block = sides[len(sides) - 1]

print(block)
for i in range(0, len(sides) + 1):
    if sides[i] > sides[len(sides) - i-1] or sides[len(sides) - i] <= sides[i]:
        if sides[i] > block:
            result = "Impossible"
        else:
            block = sides[i]
            result = "Possible"
    else:
        if sides[len(sides) - i] > block:
            result = "Impossible"
        else:
            block = sides[len(sides) - i]
            result = "Possible"

# noinspection PyUnboundLocalVariable
print(result)
