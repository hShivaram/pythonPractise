n = int(input())

pascal = []


def summ(n):
    sm = 0
    for i in range(n):
        sm += i
    return sm


def binomialCoeff(num, k):
    res = 1
    if k > num - k:
        k = num - k
    for i in range(0, k):
        res = res * (num - i)
        res = res // (i + 1)

    return res


def printPascal(num):
    # Iterate through every line
    # and print entries in it
    for line in range(0, num):

        for i in range(0, line + 1):
            pascal.append(binomialCoeff(line, i))

        print()


printPascal(n)

print(pascal[summ(n):])
