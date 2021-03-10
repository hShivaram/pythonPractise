n=int(input())
sum=0
my_list=['0','1']
for i in range(1,n+1):
    sum=int(my_list[i])+int(my_list[i-1])
    my_list.append(sum)

for i in range(n):
    print(my_list[i])
