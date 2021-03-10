#please take input here
n=int(input())

#start writing your code here
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i-1):
        print("*_",end="")
    print("*")