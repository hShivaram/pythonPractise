n=int(input())

sum=0
#mylist=[]
for i in range(2,n+1):
    count = 0
    for j in range(2,i+1):
        if(i%j ==0 and i !=j):
            count+=1
            break
    if(count==0):
        sum+=i

print(sum)