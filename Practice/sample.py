n = int(input())
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets[0])
# start writing your code here
# for i in range(0,n+1):
#        print('-'*n,end='')
#        for j in range(i):
#               print(alphabets[n-1],end="")
# print('-', end='')
row = n + (n - 1)
col = 2 * row
for i in range(row):
    for j in range(col):
        if j == (col // 2):
            print(alphabets[n - 1], end="")
        print("-", end="")
    print()
    n = n - 1
