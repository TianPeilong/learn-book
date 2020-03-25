from typing import List
from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        init = [0,1,1]
        if n < 4:
            return init[n-1]
        q = deque()
        q.extend(init)
        s = 2
        while n > 3:
            q.append(s)
            s += s
            s -= q.popleft()
            n -= 1
        return s % (2**31)