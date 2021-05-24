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


print(precision(10))
print(expo(10))