input_list=[1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]
d= {}
 # start writing your code from here
for i in range(len(input_list)):
    for j in range(0, len(input_list)):
        if input_list[i] == input_list[j] and i !=j:
            if input_list[i] not in d.keys():
                d[input_list[i]] = j-i-1
            elif j > d[input_list[i]] and input_list[i] in d.keys():
                d[input_list[i]] = j-1

for i in input_list:
    if i not in d.keys():
        d[i] = 0

print(max(d.values()))