from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return True
        start = 1
        while start < len(A) and A[start] == A[start-1]:
            start += 1
        if start >= len(A):
            return True
        d = A[start] > A[start-1]
        for i in range(start,len(A)):
            if A[i] == A[i-1]:
                continue
            if (A[i] > A[i-1]) != d:
                return False
        return True

s = Solution()
A = [6,5,4,4]
print(s.isMonotonic(A))