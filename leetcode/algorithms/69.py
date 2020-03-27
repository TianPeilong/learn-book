class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        l = 1
        r = x // 2
        while l <= r:
            m = (l + r) // 2
            y = m**2
            if y == x:
                return m
            elif y < x:
                l = m + 1
            else:
                r = m - 1
        return min(l,r)

s = Solution()
print(s.mySqrt(8))