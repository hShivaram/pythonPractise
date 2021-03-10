row=int(input())
col=int(input())

orginal_list=[]
#start writing code here
for i in range(row):
    list = []
    for j in range(col):
        list.append(0)
    orginal_list.append(list)

print(orginal_list)