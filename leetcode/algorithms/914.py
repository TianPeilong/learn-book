from typing import List

from collections import Counter
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x, y):
            if x == y:
                return x
            ox = x % 2 == 0
            oy = y % 2 == 0
            if ox and oy:
                return 2 * gcd(x>>1, y>>1)
            elif ox:
                return gcd(x>>1, y)
            elif oy:
                return gcd(x, y>>1)
            else:
                return gcd(y-x,x) if y > x else gcd(x-y,y)

        counts = Counter(deck).values()
        return reduce(gcd,counts) >= 2



# 辗转相除
def gcd(x, y):
    return y if x == 0 else gcd(y%x, x)

# 更相减损术
def gcd1(x, y):
    if x == y:
        return x
    else:
        return gcd1(y-x,x) if y > x else gcd1(x-y,y)

# 更相减损术与移位结合
def gcd2(x, y):
    if x == y:
        return x
    ox = not (x & 1)
    oy = not (y & 1)
    if ox and oy:
        return 2 * gcd2(x>>1, y>>1)
    elif ox:
        return gcd2(x>>1, y)
    elif oy:
        return gcd2(x, y>>1)
    else:
        return gcd2(y-x,x) if y > x else gcd2(x-y,y)


x = 100
y = 38764

print(gcd(y, x))
print(gcd1(x, y))
print(gcd2(x, y))

'''
s = Solution()
deck = [1,1,1,2,2,2,3,3]
print(s.hasGroupsSizeX(deck))
'''