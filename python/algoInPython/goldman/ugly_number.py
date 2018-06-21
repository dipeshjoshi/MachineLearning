



def maxDivisible(a, b):
    while a%b == 0:
        a = a/b
    return a


def isUgly(number):
    number = maxDivisible(number, 2)
    number = maxDivisible(number, 3)
    number = maxDivisible(number, 5)
    if number == 1:
        return 1
    else:
        return 0



def findNthUglyNumber(n):
    ugly_count = 1
    number = 1
    while ugly_count < n:
        number += 1
        result = isUgly(number)
        if result == 1:
            ugly_count += 1
    print number


n = 150
findNthUglyNumber(n)
