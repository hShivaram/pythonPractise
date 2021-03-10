import string
n = int(input())

# Write your code below
a = string.ascii_lowercase
List = []
for i in range(n):
    s = "-".join(a[i:n])
    #print(s)
    #print("slicing ",s[::-1],"one more slicing",s[1:])
    List.append(s[::-1] + s[1:])
#print(List)
width = len(List[0])

for i in range(n-1, 0, -1):
    #print(i)
    print(List[i].center(width, "-"))

for i in range(n):
    print(List[i].center(width, "-"))