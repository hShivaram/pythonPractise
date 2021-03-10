# You will be given a number. You have to reverse the digits of the number and print it.

# take input of the number here
inp = int(input())
r = 0
# write code to reverse the number here
while inp > 0:
    r = r * 10 + inp % 10
    inp = inp // 10
print(r)




