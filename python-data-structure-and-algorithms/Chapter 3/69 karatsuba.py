from math import log10
import math
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y
    n = max(int(log10(x)+1), int(log10(y)+1))
    n_2 = int(math.ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd
    return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc)))

import random
def test():
    for i in range(1000):
        x = random.randint(1, 10**5)
        y = random.randint(1, 10**5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return 'Failed!'
    return 'ok!'

print(test())