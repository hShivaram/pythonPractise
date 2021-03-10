n=int(input())
sum=0
digits = [int(x) for x in str(n)]
#print(digits)
for i in range(len(digits)):
    sum+=(digits[i]**3)
    #print(i,sum)
#print(sum)
if(sum==n):
    print("True")
else:
    print("False")