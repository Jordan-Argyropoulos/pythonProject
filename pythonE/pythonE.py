from math import factorial
from math import e


def expo(n):
    ex, k = 1, 0
    while abs(ex - e) > 10 ** (-n):
        k += 1
        ex += 1 / factorial(k)
    return ex, k


def precision(p):
    ex, k = expo(p)
    return ex, e, abs(ex - e), k


def euler(first, second, third, four, five, six, seven, eight):
    euler_number = 0
    arg = 1
    if(euler_number == 0):
        first = 1 / factorial(arg)
        euler_number = euler_number + 1
        arg = arg + 1
        print(first)
    if(euler_number == 1):
        second = 1 / factorial(arg)
        euler_number = euler_number + 1
        arg = arg + 1
        print(first)




print(precision(10))
print(expo(10))

euler(2, 4, 6, 8, 10, 12, 14, 17)
