from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        b = [0] * 1001
        for x in arr1:
            i = x - 1
            b[i] = b[i] + 1
        result = []
        for x in arr2:
            i = x - 1
            result.extend([x] * b[i])
            b[i] = 0
        for i,x in enumerate(b):
            if x > 0:
                result.extend([i+1]*x)
        return result