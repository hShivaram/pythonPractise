import ast

input_list = ast.literal_eval(input())


for i in range(1, len(input_list)):

    key = input_list[i]
    j = i-1

    while j >= 0 and key < input_list[j]:
        input_list[j+1] = input_list[j]
        j -= 1
    input_list[j+1] = key

print(input_list)